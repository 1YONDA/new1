# compress
# b64encode

import base64
import zlib

long_text = 'Архивация текста и разархивация'
print('long_text', len(long_text))

long_text_compressed = zlib.compress(long_text.encode('utf-8'))

print('long_text_compressed', len(long_text_compressed))

long_text_compressed_b64 = base64.b64encode(long_text_compressed)

print('long_text_compressed_b64', len(long_text_compressed_b64))

decoded_b64_text = base64.b64decode(long_text_compressed_b64)
undompressed_text = zlib.decompress(decoded_b64_text).decode('utf-8')

print(undompressed_text)
