WebPsi
======

A Python web app to aid psychic abilities experiments.

This is the version used by Randonautica and requires access to the official Firestore database. 

Please use the [public original version](https://github.com/AndieNoir/WebPsi)

Installation
------------

1. Run the following commands

   ```
   pip3 install -r requirements.txt
   ```

2. Create an `.env` file and add the Firebase credentials:

   ```
   FIREBASE_APIKEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   FIREBASE_AUTHDOMAIN=xxxxxxxxxxxxxxxxxx.firebaseapp.com
   FIREBASE_DATABASEURL=https://xxxxxxxxxxxxxxxxxx.firebaseio.com
   FIREBASE_STORAGEBUCKET=xxxxxxxxxxxxxxxxxx.appspot.com
   ```

Running
-------

1. Run the following command for testing

   ```
   python3 -m webpsi
   ```

2. Build as Docker container using

   ```
   docker compose up
   ```

3. Open http://localhost:58700

License
-------

    Copyright (C) 2020 AndieNoir
    
    WebPsi is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    WebPsi is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with WebPsi.  If not, see <https://www.gnu.org/licenses/>.
