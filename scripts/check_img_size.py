import struct
import os

def get_png_dimensions(file_path):
    with open(file_path, 'rb') as f:
        # Check PNG signature
        if f.read(8) != b'\x89PNG\r\n\x1a\n':
            return None
        
        # Read IHDR chunk
        # Length (4), Type (4), Data (13), CRC (4)
        # IHDR is the first chunk
        chunk_len_bytes = f.read(4)
        chunk_type = f.read(4)
        
        if chunk_type != b'IHDR':
            return None
            
        width = struct.unpack('>I', f.read(4))[0]
        height = struct.unpack('>I', f.read(4))[0]
        
        return width, height

file_paths = [
    r'd:\KYY\jingxiutuku-15\src\assets\img\touxiang-banner.png',
    r'd:\KYY\jingxiutuku-15\src\assets\img\biaoqiangbao-banner.png',
    r'd:\KYY\jingxiutuku-15\src\assets\img\shouye-banner-1.png'
]

for file_path in file_paths:
    try:
        dims = get_png_dimensions(file_path)
        if dims:
            print(f"File: {os.path.basename(file_path)}, Width: {dims[0]}, Height: {dims[1]}")
        else:
            print(f"File: {os.path.basename(file_path)}, Could not read dimensions")
    except Exception as e:
        print(f"File: {os.path.basename(file_path)}, Error: {e}")
