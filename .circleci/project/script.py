import os
import yaml

def deploy_to_s3(s3_bucket_path, s3_key, local_file):
    cmd = f"aws s3 cp {local_file} s3://{s3_bucket_path}/{s3_key}"
    print("Running command: ", cmd)
    os.system(cmd)

if __name__ == "__main__":
    # Load the config file
    with open('config.yml') as f:
        config = yaml.safe_load(f)

    # Example usage
    deploy_to_s3(config['s3']['beta_bucket'], config['s3']['index_key'], 'index.html')
    deploy_to_s3(config['s3']['prod_bucket'], config['s3']['index_key'], 'index.html')
