import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "bigproject-d6846",
    "private_key_id": "9fcf16847ffc6f34c87e9bea9d2141bdcfd60df8",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQCj3+M0t/R11epb\nC3UBvh558rKZahcOuUxxvwfU1FJMkgJSOLZy30JHJjxRpTZIS/fIgZNOe9OPL77g\nT+1CG94Z817s6xOpuX4uPntDhbgJx87n322J7MtTL9bzouoNovsFyZi183Mb9+7A\n44kbdBw1iB7o+FYFE8d2Xrxjmf1UErVVcaXRC89pAPcKGKPYe0lsVjIR5rO7sKTk\nP2yAVJfX43gDmQD+Ysy62wi2gL73XF0YTcrQDcs4+NRzlOG05fyZyDnm7iN/GliC\n1h/caJc68t9Sg5pbHRSJj/xtfOQpz/qBMHCPwlZ1ZAIc6U/7aigcatmFdOCAjYou\nXJyLtkP5AgMBAAECggEACi6yV0dqNQYxNS4IO678sCF179VpOwd61K3aMThuKAbX\nMRUICn7ihzmSJuqSmGRsBYqTmh1UlGw9j9eM4P41SzyANKLDX9jq77mp1BS+I5Fw\nQvUdlnk0WxC5FP4VoqTytGCF5iG15dIpL4AT4rT7abzHBZJ6BH++9ZUbtJP6wIX9\nhsKge7SeuGCbf8AD5LOtB7JuocHL9C+wpwoxVVVgvsZrpJJozvclUJcwxLRlR5g4\nXfWll2HVHtinDCIf/oU4A2t6cQkccRrGFByieMTrNdhI1EqZy6y6wCGCsYNEosjP\nfA/fK2qTQ3p5omU97QYrJ+VYuz4oY1pk6b8z/ohhmQKBgQDeljBMynPRlfMqUExo\nFYPdJ5iu956a6yWX9qaLT2R/LRh1dLhKzaaLOtE25srv7OrIOslMmTajkdhuJdUE\nqQcqUReZuoqsltYBJusbmO6kkdU3THLP7nDNTvq9Cr6kqxGtp2A2JxNnEuFmNI8n\nxC/JmqJB5p6oLNqklKbk3tAnVQKBgQC8eXGSS+rv5lqj1H5wQFkUsahbqdcVGJwY\n5mtUtJYmwqvtkmfL/eE8GYu66fJEA4HrJdVTI4uhx4RHczeVVrrsRS4yxorqCE3y\nvTMua8/ILZ3Gv/Qjr+VYGJvL88GKBOmuf/oKUcY53e6jBQQq/G6cHIRf99c9FUa6\n4n2a5kLiFQJ/e3bTU8T4eUizmMTxnMpSWlmcV3ECiOvl7mTh/GQNWn2pE32qu9NW\njeQSKGHcLzk7AdWZ0uMpa5F6e56AihU35EEW1i6ivRjtm7X6s1QhCyfZHNNK3Atm\nhntImZNcK/q305sDwwXpvUK7w/Vjcqtf1nPvjJ5fYul+XcwWxtzQmQKBgDN13UKa\no+0YskrlLBiuGSSDVXqhpu5Fp+lMkKWyIQU4RgU54klaanMkbnh8g/96DbEMxXBL\n1kY32bBAjz6hTaxRP0nx1+AKoG3UpvLX0QXRHrEznA9aaX5iSbeoOIHc0YkpvDWx\nGjSWmh+8sOSjw/ev+ZzSaNxuwL8qNC1lDYH5AoGADtKFgAu0Qvzw6XF5SQLbZVkV\nez33hzW02oDkJpkEWbp/jrXOK/Gn7MLITmQzJEp5t0GO3jPEAF8RQq02l4wfHDdI\nSolnVJfdJPeyBSG9M0GoCx6l2DYaz6SpSKxqewop5SoHJPitMsSF5z5+wNP1+Bxh\nex8B8hV44ILpcuHBqCU=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-r6qtg@bigproject-d6846.iam.gserviceaccount.com",
    "client_id": "111907533834759119723",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-r6qtg%40bigproject-d6846.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})
firebase_admin.initialize_app(cred)