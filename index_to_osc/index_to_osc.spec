# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'bindings', 'bindings' ),
         ( 'config.json.template', '.' ),
         ]
a = Analysis(['index_to_osc.py'],
             pathex=['C:\\Users\\Marian\\Desktop\\VRCHAT_LAUNCH_ADDONS\\index_controller_bypasser\\index_to_osc'],
             binaries=[ (r'C:\Users\Marian\Desktop\VRCHAT_LAUNCH_ADDONS\index_controller_bypasser\venv\Lib\site-packages\openvr\libopenvr_api_64.dll', '.' ), ],
             datas = added_files,
             hiddenimports=['ctypes'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='index_to_osc',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='index_to_osc')
