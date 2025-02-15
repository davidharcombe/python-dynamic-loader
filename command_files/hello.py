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
from typing import Mapping
from dynamic import DynamicClass


class HelloWorld(DynamicClass):
  """A simple dynamic Hello World."""

  def run(self, **attributes: Mapping[str, str]) -> str:
    """Runs the command.

    The is the mandatory implementation of the `run` method in `DynamicClass`.
    It is the only method that the framework will call.

    The attributes are passed as Python keyword args and will vary according to
    whatever the user needs.

    Returns:
        Dict[str, Any]: the result of the command
    """
    return "Hello world!"
