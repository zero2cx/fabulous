#!/usr/bin/env python
#
# Copyright 2016 The Fabulous Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is a long timed progress bar. Don't expect it to finish any 
time soon. It updates every 0 to 10 seconds. Send it a keyboard 
interupt (Ctrl-C) to stop."""

from fabulous.widget import TimedProgressBar
import time
import random

print __doc__

p = TimedProgressBar('bar')
p.precision=10000
n = 100000
for i in range(n):
    p.update(float(i)/n *100, 'update '+str(i))
    time.sleep(random.random()* 10)
