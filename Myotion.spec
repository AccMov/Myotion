# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        # 目录资源 ↓
        ('images/**/*', 'images'),
        ('themes/*', 'themes'), 
        ('widgets/**/*', 'widgets'),
        ('myotion_resources/*', 'myotion_resources'),
        ('shiny/**/*', 'shiny'),

        # 单文件资源 ↓
        ('*.ui', '.'),
        ('*.qrc', '.'),
        ('*.png', 'icons'),
        ('*.ico', 'icons'),
    ],
    hiddenimports=[
        # Qt 相关 ↓
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtWebEngineCore',
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtQuick',
        
        # 数据科学相关 ↓
        'scipy.signal.spectral',
        'pandas._libs.tslibs',
        
        # 项目模块 ↓
        'modules.*', 
        'script.*',
        'shiny.*',
        'widgets.*'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

# Qt WebEngine 运行时特殊处理 ↓
qwebengine = [
    (a.binaries[-1][0], a.binaries[-1][1], 'BINARY'),
    (a.datas[-1][0], a.datas[-1][1], 'DATA')
]

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Myotion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Myotion_logo.ico'],
)
coll = COLLECT(
    exe,
    a.binaries + qwebengine,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Myotion'
)
