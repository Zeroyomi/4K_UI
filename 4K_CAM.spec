# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['F:\\Python_project\\Kivy\\4K_UI\\pack\\main.py'],
             pathex=['F:\\Python_project\\Kivy\\4K_UI\\pack'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
			 
a.datas += [('Code\smart.kv', 'F:\\Python_project\\Kivy\\4K_UI\\pack\\smart.kv', 'DATA')]
			 
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='4K_CAM',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe, Tree('F:\\Python_project\\Kivy\\4K_UI\\pack'),
               a.binaries,
               a.zipfiles,
               a.datas,
			   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='4K_CAM')
