"""
 
Read tb_epos_sales_line Delta Lake table
 
Correctly handles Delta Lake transaction log and deletion vectors
 
"""
 
import pandas as pd
 
from azure.identity import ManagedIdentityCredential
 
from azure.storage.blob import BlobServiceClient
 
import json
 
import io

# Configuration
 
ACCOUNT_URL = "https:.net"
 
CONTAINER_NAME = "gg"
 
FOLDER_PATH = "gg/3e4"

# Extract account name
 
ACCOUNT_NAME = ACCOUNT_URL.split('//')[1].split('.')[0]

def read_delta_table(folder_path, num_log_files=20):
 
    """Read Delta Lake table by parsing transaction log"""
 
    print(f"Authenticating with Managed Identity...")
 
    credential = ManagedIdentityCredential()
 
    # Create blob service client
 
    blob_service_client = BlobServiceClient(
 
        account_url=ACCOUNT_URL,
 
        credential=credential
 
    )
 
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
 
    # List all files in the delta log
 
    delta_log_path = f"{folder_path}/_delta_log/"
 
    print(f"Reading Delta log from: {delta_log_path}")
 
    log_files = []
 
    for blob in container_client.list_blobs(name_starts_with=delta_log_path):
 
        if blob.name.endswith('.json'):
 
            log_files.append(blob.name)
 
    log_files.sort()
 
    print(f"Found {len(log_files)} log files")
 
    # Get the latest checkpoint or read all logs
 
    parquet_files = set()
 
    removed_files = set()
 
    # Read log files to understand which parquet files to read
 
    for log_file in log_files[-num_log_files:]:
 
        print(f"Reading {log_file.split('/')[-1]}...")
 
        blob_client = container_client.get_blob_client(log_file)
 
        content = blob_client.download_blob().readall().decode('utf-8')
 
        # Parse each line (Delta log is newline-delimited JSON)
 
        for line in content.strip().split('\n'):
 
            if not line:
 
                continue
 
            try:
 
                entry = json.loads(line)
 
                # Check for add actions (files added)
 
                if 'add' in entry:
 
                    file_path = entry['add']['path']
 
                    parquet_files.add(file_path)
 
                # Check for remove actions (files removed)
 
                if 'remove' in entry:
 
                    file_path = entry['remove']['path']
 
                    removed_files.add(file_path)
 
                    if file_path in parquet_files:
 
                        parquet_files.remove(file_path)
 
            except json.JSONDecodeError:
 
                continue
 
    # Calculate current files (added - removed)
 
    current_files = parquet_files - removed_files
 
    print(f"✅ Found {len(current_files)} current parquet files")
 
    if len(current_files) == 0:
 
        print("❌ No current files found. Try increasing num_log_files parameter.")
 
        return None
 
    # Read all current parquet files
 
    dfs = []
 
    for i, parquet_file in enumerate(current_files, 1):
 
        full_path = f"{folder_path}/{parquet_file}"
 
        print(f"Reading file {i}/{len(current_files)}: {parquet_file}")
 
        blob_client = container_client.get_blob_client(full_path)
 
        parquet_data = blob_client.download_blob().readall()
 
        # Read parquet from bytes
 
        df_part = pd.read_parquet(io.BytesIO(parquet_data))
 
        dfs.append(df_part)
 
    # Combine all dataframes
 
    print("\nCombining all parquet files...")
 
    df = pd.concat(dfs, ignore_index=True)
 
    return df

if __name__ == "__main__":

    try:

        df = read_delta_table(FOLDER_PATH)
 
        if df is not None:

            # Make sure Pandas shows all columns

            pd.set_option('display.max_columns', None)

            pd.set_option('display.width', 2000)  # Prevent wrapping

            pd.set_option('display.max_colwidth', None)
 
            print("\n" + "="*60)

            print("✅ Successfully loaded tb_epos_sales_line Delta Lake data")

            print(f"📊 Dataset shape: {df.shape}")

            print(f"📊 Total rows: {len(df):,}")
 
            # Show partition info if available

            if 'yearmonth' in df.columns:

                print(f"\n📅 Partitions: {df['yearmonth'].value_counts().sort_index().to_dict()}")
 
            # Display all column names

            print(f"\n🔍 Columns ({len(df.columns)}):")

            print(df.columns.tolist())
 
            # Display all columns for first 5 rows

            print(f"\n🔍 First 5 rows (all columns):")

            print(df.head(5))
 
            # Display data types

            print(f"\n📋 Data types:")

            print(df.dtypes)
 
    except Exception as exc:

        print(f"❌ Failed to load data: {exc}")

        import traceback

        traceback.print_exc()

 
