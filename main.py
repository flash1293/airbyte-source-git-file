#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_git_file import SourceGitFile

if __name__ == "__main__":
    source = SourceGitFile()
    launch(source, sys.argv[1:])
