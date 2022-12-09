"""
command line interface for azb
"""

import os
import argparse
from . import azb

# storage_account_name = os.environ["AZ_STORAGE_ACCOUNT_NAME"]
# storage_account_key = os.environ["AZ_STORAGE_ACCOUNT_KEY"]


AZ_VAR_ENV = dict(
    SA_NAME=["storage_account_name", "AZ_STORAGE_ACCOUNT_NAME"],
    SA_KEY=["storage_account_key", "AZ_STORAGE_ACCOUNT_KEY"],
    BC_NAME=["blob_container_name", "AZ_BLOB_CONTAINER_NAME"],
    SAS=["sas_token", "AZ_SAS_TOKEN"],
)


def get_var_from_args(args, item):
    azv, aze = AZ_VAR_ENV[item]
    ret = getattr(args, azv)

    # if an argument for the item is not given in command line arguments,
    # retrieve a value from an environment variable
    if not ret:
        try:
            ret = os.environ[aze]
        except KeyError as e:
            print(f"The environment variable {e.args[0]} is not defined!")
            raise
    return ret


def get_azcontainer(args):
    storage_account_name = get_var_from_args(args, "SA_NAME")
    container_name = get_var_from_args(args, "BC_NAME")
    sas_token = get_var_from_args(args, "SAS")

    azcontainer = azb.AZCONTAINER(
        storage_account_name, container_name, sas_token
    )

    return azcontainer


def get_sas(args):
    storage_account_name = get_var_from_args(args, "SA_NAME")
    storage_account_key = get_var_from_args(args, "SA_KEY")

    sas_token = azb.get_sas(storage_account_name, storage_account_key, args.ttl)
    print(sas_token)


def list_blobs(args):
    azcontainer = get_azcontainer(args)
    blobs = azcontainer.list_blobs()
    for b in blobs:
        print(b)


def upload_blob(args):
    azcontainer = get_azcontainer(args)
    azcontainer.upload_blob(args.blob_name, args.file_name)


def download_blob(args):
    azcontainer = get_azcontainer(args)
    azcontainer.download_blob(args.blob_name, args.file_name)


def delete_blob(args):
    azcontainer = get_azcontainer(args)
    azcontainer.delete_blob(args.blob_name)


def main():
    parser = argparse.ArgumentParser(description="azure blob storage utility")

    subparsers = parser.add_subparsers(
        dest="subparser_name",
        title="subcommands",
        description="valid subcomands",
        help="additional help",
    )

    ## common optional arguments
    common_opt_arg_parser = argparse.ArgumentParser(add_help=False)
    common_opt_arg_parser.add_argument(
        "-san", "--storage_account_name", help="storage account name"
    )
    common_opt_arg_parser.add_argument(
        "-bcn", "--blob_container_name", help="container name"
    )
    common_opt_arg_parser.add_argument("-st", "--sas_token", help="SAS token")

    ## get sas
    parser_get_sas = subparsers.add_parser("get_sas", help="get sas")
    parser_get_sas.add_argument(
        "-san", "--storage_account_name", help="azure storage account name"
    )
    parser_get_sas.add_argument(
        "-sak", "--storage_account_key", help="storage account key"
    )
    parser_get_sas.add_argument(
        "-t",
        "--ttl",
        type=int,
        default=1,
        help="time to live; should be specified in hour",
    )
    parser_get_sas.set_defaults(func=get_sas)

    ## list blobs
    parser_list_blobs = subparsers.add_parser(
        "list_blobs", parents=[common_opt_arg_parser], help="list blobs"
    )
    parser_list_blobs.set_defaults(func=list_blobs)

    ## upload blob
    parser_upload_blob = subparsers.add_parser(
        "upload_blob", parents=[common_opt_arg_parser], help="upload blob"
    )
    parser_upload_blob.add_argument("blob_name", help="blob name")
    parser_upload_blob.add_argument(
        "file_name", help="the name of a file to be uploaded"
    )
    parser_upload_blob.set_defaults(func=upload_blob)

    ## download blob
    parser_download_blob = subparsers.add_parser(
        "download_blob", parents=[common_opt_arg_parser], help="download blob"
    )
    parser_download_blob.add_argument("blob_name", help="blob name")
    parser_download_blob.add_argument(
        "file_name",
        help="the name of a file in which a downloaded blob is saved",
    )
    parser_download_blob.set_defaults(func=download_blob)

    ## delete blob
    parser_delete_blob = subparsers.add_parser(
        "delete_blob", parents=[common_opt_arg_parser], help="delete blob"
    )
    parser_delete_blob.add_argument("blob_name", help="blob name")
    parser_delete_blob.set_defaults(func=delete_blob)

    # execute
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
