import zlib,base64
exec(zlib.decompress(base64.b64decode(b'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')))
