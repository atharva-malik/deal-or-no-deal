# Test Cases for my script

### Cases for login
##### Data:
```json
{"atharva.malik": {"password": "admin"}, "asdf": {"password": "asdf"}, "1234567890": {"password": "1234567890"}}
```
##### Case 1:
###### Input:
```json
Username: atharva
Password: admin
Output: Failed
```
##### Case 2:
###### Input:
```json
Username: atharva.malik
Password: admin
Output: Authenticated
```



### Cases for signup
##### Data:
```json
{"admin": {"password": "admin"}, "asdf": {"password": "asdf"}}
```
##### Case 1:
###### Input:
```json
Username: admin
Password: 1234
Output: Username taken.
Dataset remains unchanged
```
##### Case 2:
###### Input:
```json
Username: atharva.malik
Password: admin
Output: Redirect to login.
Data: {"admin": {"password": "admin"}, "asdf": {"password": "asdf"}, "atharva.malik": {"password": "admin"}}
```
