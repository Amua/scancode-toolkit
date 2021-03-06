#
# Copyright (c) 2015 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import, print_function

import os

from commoncode.testcase import FileBasedTesting

from commoncode.hash import b64sha1
from commoncode.hash import get_hasher
from commoncode.hash import md5
from commoncode.hash import sha1
from commoncode.hash import sha256
from commoncode.hash import sha512


class TestHash(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_get_hasher(self):
        h = get_hasher(160)
        assert 'hvfkN_qlp_zhXR3cuerq6jd2Z7g=' == h('a').b64digest()
        assert '4MkDWJjdUvxlxBRUzsnE0mEb-zc=' == h('aa').b64digest()
        assert 'fiQN50-x7Qj6CNOAY_amqRRiqBU=' == h('aaa').b64digest()

    def test_short_hashes(self):
        h = get_hasher(32)
        assert '0cc175b9' == h('a').hexdigest()
        assert '4124bc0a' == h('aa').hexdigest()
        h = get_hasher(64)
        assert '4124bc0a9335c27f' == h('aa').hexdigest()

    def test_sha1_checksum(self):
        test_file = self.get_test_loc('hash/dir1/a.png')
        assert sha1(test_file) == '34ac5465d48a9b04fc275f09bc2230660df8f4f7'

    def test_sha1_checksum_on_text(self):
        test_file = self.get_test_loc('hash/dir1/a.txt')
        assert sha1(test_file) == '3ca69e8d6c234a469d16ac28a4a658c92267c423'

    def test_sha1_checksum_on_text2(self):
        test_file = self.get_test_loc('hash/dir2/a.txt')
        assert sha1(test_file) == '3ca69e8d6c234a469d16ac28a4a658c92267c423'

    def test_sha1_checksum_on_dos_text(self):
        test_file = self.get_test_loc('hash/dir2/dos.txt')
        assert sha1(test_file) == 'a71718fb198630ae8ba32926015d8555a03cb06c'

    def test_sha1_checksum_base64(self):
        test_file = self.get_test_loc('hash/dir1/a.png')
        assert b64sha1(test_file) == 'NKxUZdSKmwT8J18JvCIwZg349Pc='

    def test_md5_checksum(self):
        test_file = self.get_test_loc('hash/dir1/a.png')
        assert md5(test_file) == '4760fb467f1ebf3b0aeace4a3926f1a4'

    def test_md5_checksum_on_text(self):
        test_file = self.get_test_loc('hash/dir1/a.txt')
        assert md5(test_file) == '40c53c58fdafacc83cfff6ee3d2f6d69'

    def test_md5_checksum_on_text2(self):
        test_file = self.get_test_loc('hash/dir2/a.txt')
        assert md5(test_file) == '40c53c58fdafacc83cfff6ee3d2f6d69'

    def test_md5_checksum_on_dos_text(self):
        test_file = self.get_test_loc('hash/dir2/dos.txt')
        assert md5(test_file) == '095f5068940e41df9add5d4cc396c181'

    def test_sha256_checksum(self):
        test_file = self.get_test_loc('hash/dir1/a.png')
        assert sha256(test_file) == '1b598db6fee8f1ec7bb919c0adf68956f3d20af8c9934a9cf2db52e1347efd35'

    def test_sha512_checksum(self):
        test_file = self.get_test_loc('hash/dir1/a.png')
        assert sha512(test_file) == '5be9e01cd20ff288fd3c3fc46be5c2747eaa2c526197125330947a95cdb418222176b182a4680f0e435ba8f114363c45a67b30eed9a9222407e63ccbde46d3b4'
