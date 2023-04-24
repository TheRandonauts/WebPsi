# Copyright (C) 2020 AndieNoir
#
# WebPsi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# WebPsi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with WebPsi.  If not, see <https://www.gnu.org/licenses/>.

import os
from dotenv import load_dotenv

from webpsi.generator.rndo_comscire import Randonautica_QRNG

load_dotenv()

GENERATOR_CLASS = Randonautica_QRNG
FIREBASE_CONFIG = {
    "apiKey": os.environ.get("FIREBASE_APIKEY"),
    "authDomain": os.environ.get("FIREBASE_AUTHDOMAIN"),
    "databaseURL": os.environ.get("FIREBASE_DATABASEURL"),
    "storageBucket": os.environ.get("FIREBASE_STORAGEBUCKET"),
}