# Copyright 2023 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Any, Mapping, Union

from dynamic import DynamicClass
from dynamic import LocalStorage, SecretManager, CloudStorage


def main(unused_argv):
  """Used for testing.

  Args:
      unused_argv (List[Any]): unused
  """
  try:
    # To use secret manager instead, simply change 'storage=CloudStorage'
    # to read 'storage=SecretManager'. All the imports have been left in place
    # above to make this as easy as possible.
    processor = DynamicClass.install(module_name='hello',
                                     class_name='HelloWorld',
                                     storage=LocalStorage,
                                     bucket='[MY BUCKET NAME]',
                                     folder='command_files')
    print(processor().run(attributes=dict()))

  except Exception as e:
    print(f'Exception in command processor: {e}')



if __name__ == '__main__':
  main([])
