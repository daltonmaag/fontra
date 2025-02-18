import contextlib
from importlib.metadata import entry_points
import pathlib
import pytest


dataDir = pathlib.Path(__file__).resolve().parent / "data"


getGlyphTestData = [
    (
        "ufo",
        {
            "name": "period",
            "unicodes": [ord(".")],
            "sources": [
                {
                    "location": {},
                    "layerName": "foreground",
                }
            ],
            "layers": [
                {
                    "name": "foreground",
                    "glyph": {
                        "xAdvance": 170,
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [60, 0, 110, 0, 110, 120, 60, 120],
                            "pointTypes": [0, 0, 0, 0],
                        },
                    },
                },
                {
                    "name": "background",
                    "glyph": {
                        "xAdvance": 170,
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [62, 0, 112, 0, 112, 120, 62, 120],
                            "pointTypes": [0, 0, 0, 0],
                        },
                    },
                },
            ],
        },
    ),
    (
        "ufo",
        {
            "name": "Aacute",
            "unicodes": [ord("Á"), ord("á")],
            "sources": [
                {
                    "location": {},
                    "layerName": "foreground",
                }
            ],
            "layers": [
                {
                    "name": "foreground",
                    "glyph": {
                        "components": [
                            {
                                "name": "A",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 0,
                                    "y": 0,
                                },
                            },
                            {
                                "name": "acute",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 99,
                                    "y": 20,
                                },
                            },
                        ],
                        "xAdvance": 396,
                    },
                },
            ],
        },
    ),
    (
        "designspace",
        {
            "name": "period",
            "unicodes": [ord(".")],
            "sources": [
                {
                    "name": "LightCondensed",
                    "location": {"weight": 150.0, "width": 0.0},
                    "layerName": "LightCondensed/foreground",
                },
                {
                    "name": "BoldCondensed",
                    "location": {"weight": 850.0, "width": 0.0},
                    "layerName": "BoldCondensed/foreground",
                },
                {
                    "name": "LightWide",
                    "location": {"weight": 150.0, "width": 1000.0},
                    "layerName": "LightWide/foreground",
                },
                {
                    "name": "BoldWide",
                    "location": {"weight": 850.0, "width": 1000.0},
                    "layerName": "BoldWide/foreground",
                },
            ],
            "layers": [
                {
                    "name": "LightCondensed/foreground",
                    "glyph": {
                        "xAdvance": 170,
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [60, 0, 110, 0, 110, 120, 60, 120],
                            "pointTypes": [0, 0, 0, 0],
                        },
                    },
                },
                {
                    "name": "LightCondensed/background",
                    "glyph": {
                        "xAdvance": 170,
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [62, 0, 112, 0, 112, 120, 62, 120],
                            "pointTypes": [0, 0, 0, 0],
                        },
                    },
                },
                {
                    "name": "BoldCondensed/foreground",
                    "glyph": {
                        "xAdvance": 250,
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [30, 0, 220, 0, 220, 300, 30, 300],
                            "pointTypes": [0, 0, 0, 0],
                        },
                    },
                },
                {
                    "name": "LightWide/foreground",
                    "glyph": {
                        "xAdvance": 290,
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [120, 0, 170, 0, 170, 220, 120, 220],
                            "pointTypes": [0, 0, 0, 0],
                        },
                    },
                },
                {
                    "name": "BoldWide/foreground",
                    "glyph": {
                        "xAdvance": 310,
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [60, 0, 250, 0, 250, 300, 60, 300],
                            "pointTypes": [0, 0, 0, 0],
                        },
                    },
                },
            ],
        },
    ),
    (
        "designspace",
        {
            "name": "Aacute",
            "unicodes": [ord("Á"), ord("á")],
            "sources": [
                {
                    "name": "LightCondensed",
                    "location": {"weight": 150.0, "width": 0.0},
                    "layerName": "LightCondensed/foreground",
                },
                {
                    "name": "BoldCondensed",
                    "location": {"weight": 850.0, "width": 0.0},
                    "layerName": "BoldCondensed/foreground",
                },
                {
                    "name": "LightWide",
                    "location": {"weight": 150.0, "width": 1000.0},
                    "layerName": "LightWide/foreground",
                },
                {
                    "name": "BoldWide",
                    "location": {"weight": 850.0, "width": 1000.0},
                    "layerName": "BoldWide/foreground",
                },
            ],
            "layers": [
                {
                    "name": "LightCondensed/foreground",
                    "glyph": {
                        "components": [
                            {
                                "name": "A",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 0,
                                    "y": 0,
                                },
                            },
                            {
                                "name": "acute",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 99,
                                    "y": 20,
                                },
                            },
                        ],
                        "xAdvance": 396,
                    },
                },
                {
                    "name": "BoldCondensed/foreground",
                    "glyph": {
                        "components": [
                            {
                                "name": "A",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 0,
                                    "y": 0,
                                },
                            },
                            {
                                "name": "acute",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 204,
                                    "y": 0,
                                },
                            },
                        ],
                        "xAdvance": 740,
                    },
                },
                {
                    "name": "LightWide/foreground",
                    "glyph": {
                        "components": [
                            {
                                "name": "A",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 0,
                                    "y": 0,
                                },
                            },
                            {
                                "name": "acute",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 494,
                                    "y": 20,
                                },
                            },
                        ],
                        "xAdvance": 1190,
                    },
                },
                {
                    "name": "BoldWide/foreground",
                    "glyph": {
                        "components": [
                            {
                                "name": "A",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 0,
                                    "y": 0,
                                },
                            },
                            {
                                "name": "acute",
                                "transformation": {
                                    "rotation": 0.0,
                                    "scalex": 1.0,
                                    "scaley": 1.0,
                                    "tcenterx": 0,
                                    "tcentery": 0,
                                    "x": 484,
                                    "y": 20,
                                },
                            },
                        ],
                        "xAdvance": 1290,
                    },
                },
            ],
        },
    ),
    (
        "ttf",
        {
            "name": "period",
            "unicodes": [ord(".")],
            "layers": [
                {
                    "glyph": {
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [60, 0, 60, 120, 110, 120, 110, 0],
                            "pointTypes": [0, 0, 0, 0],
                        },
                        "xAdvance": 170,
                    },
                    "name": "<default>",
                },
                {
                    "glyph": {
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [120, 0, 120, 220, 170, 220, 170, 0],
                            "pointTypes": [0, 0, 0, 0],
                        },
                        "xAdvance": 290,
                    },
                    "name": "wdth=1",
                },
                {
                    "glyph": {
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [60, 0, 60, 300, 250, 300, 250, 0],
                            "pointTypes": [0, 0, 0, 0],
                        },
                        "xAdvance": 310,
                    },
                    "name": "wdth=1,wght=1",
                },
                {
                    "glyph": {
                        "path": {
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                            "coordinates": [30, 0, 30, 300, 220, 300, 220, 0],
                            "pointTypes": [0, 0, 0, 0],
                        },
                        "xAdvance": 250,
                    },
                    "name": "wght=1",
                },
            ],
            "sources": [
                {
                    "layerName": "<default>",
                    "location": {"wdth": 0, "wght": 0},
                    "name": "<default>",
                },
                {
                    "layerName": "wdth=1",
                    "location": {"wdth": 1.0, "wght": 0},
                    "name": "wdth=1",
                },
                {
                    "layerName": "wdth=1,wght=1",
                    "location": {"wdth": 1.0, "wght": 1.0},
                    "name": "wdth=1,wght=1",
                },
                {
                    "layerName": "wght=1",
                    "location": {"wdth": 0, "wght": 1.0},
                    "name": "wght=1",
                },
            ],
        },
    ),
    (
        "otf",
        {
            "name": "period",
            "unicodes": [46],
            "layers": [
                {
                    "name": "<default>",
                    "glyph": {
                        "path": {
                            "coordinates": [60, 0, 110, 0, 110, 120, 60, 120],
                            "pointTypes": [0, 0, 0, 0],
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                        },
                        "xAdvance": 170,
                    },
                },
                {
                    "name": "wdth=1",
                    "glyph": {
                        "path": {
                            "coordinates": [
                                120.0,
                                0,
                                170.0,
                                0,
                                170.0,
                                220.0,
                                120.0,
                                220.0,
                            ],
                            "pointTypes": [0, 0, 0, 0],
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                        },
                        "xAdvance": 290.0,
                    },
                },
                {
                    "name": "wdth=1,wght=1",
                    "glyph": {
                        "path": {
                            "coordinates": [
                                60.0,
                                0,
                                250.0,
                                0,
                                250.0,
                                300.0,
                                60.0,
                                300.0,
                            ],
                            "pointTypes": [0, 0, 0, 0],
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                        },
                        "xAdvance": 310.0,
                    },
                },
                {
                    "name": "wght=1",
                    "glyph": {
                        "path": {
                            "coordinates": [
                                30.0,
                                0,
                                220.0,
                                0,
                                220.0,
                                300.0,
                                30.0,
                                300.0,
                            ],
                            "pointTypes": [0, 0, 0, 0],
                            "contourInfo": [{"endPoint": 3, "isClosed": True}],
                        },
                        "xAdvance": 250.0,
                    },
                },
            ],
            "sources": [
                {
                    "location": {"wdth": 0, "wght": 0},
                    "name": "<default>",
                    "layerName": "<default>",
                },
                {
                    "location": {"wdth": 1.0, "wght": 0},
                    "name": "wdth=1",
                    "layerName": "wdth=1",
                },
                {
                    "location": {"wdth": 1.0, "wght": 1.0},
                    "name": "wdth=1,wght=1",
                    "layerName": "wdth=1,wght=1",
                },
                {
                    "location": {"wdth": 0, "wght": 1.0},
                    "name": "wght=1",
                    "layerName": "wght=1",
                },
            ],
        },
    ),
]


testFontPaths = {
    "designspace": dataDir / "mutatorsans" / "MutatorSans.designspace",
    "ufo": dataDir / "mutatorsans" / "MutatorSansLightCondensed.ufo",
    "ttf": dataDir / "mutatorsans" / "MutatorSans.ttf",
    "otf": dataDir / "mutatorsans" / "MutatorSans.otf",
}


def getTestFont(backendName):
    backendEntryPoints = entry_points(group="fontra.filesystem.backends")
    cls = backendEntryPoints[backendName].load()
    return cls.fromPath(testFontPaths[backendName])


getGlyphNamesTestData = [
    ("designspace", 49, ["A", "Aacute", "Adieresis", "B"]),
    ("ufo", 49, ["A", "Aacute", "Adieresis", "B"]),
]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "backendName, numGlyphs, firstFourGlyphNames", getGlyphNamesTestData
)
async def test_getGlyphNames(backendName, numGlyphs, firstFourGlyphNames):
    font = getTestFont(backendName)
    with contextlib.closing(font):
        glyphNames = sorted(await font.getReverseCmap())
        assert numGlyphs == len(glyphNames)
        assert firstFourGlyphNames == sorted(glyphNames)[:4]


getReverseCmapTestData = [
    ("designspace", 49, {"A": [ord("A"), ord("a")], "B": [ord("B"), ord("b")]}),
    ("ufo", 49, {"A": [ord("A"), ord("a")], "B": [ord("B"), ord("b")]}),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("backendName, numGlyphs, testMapping", getReverseCmapTestData)
async def test_getReverseCmap(backendName, numGlyphs, testMapping):
    font = getTestFont(backendName)
    with contextlib.closing(font):
        revCmap = await font.getReverseCmap()
        assert numGlyphs == len(revCmap)
        for glyphName, unicodes in testMapping.items():
            assert revCmap[glyphName] == unicodes


@pytest.mark.asyncio
@pytest.mark.parametrize("backendName, expectedGlyph", getGlyphTestData)
async def test_getGlyph(backendName, expectedGlyph):
    font = getTestFont(backendName)
    with contextlib.closing(font):
        glyph = await font.getGlyph(expectedGlyph["name"])
        assert glyph == expectedGlyph


getGlobalAxesTestData = [
    (
        "designspace",
        [
            {"defaultValue": 0.0, "maxValue": 1000.0, "minValue": 0.0, "name": "width"},
            {
                "defaultValue": 100.0,
                "maxValue": 900.0,
                "mapping": [[100.0, 150.0], [900.0, 850.0]],
                "minValue": 100.0,
                "name": "weight",
            },
        ],
    ),
    ("ufo", []),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("backendName, expectedGlobalAxes", getGlobalAxesTestData)
async def test_getGlobalAxes(backendName, expectedGlobalAxes):
    font = getTestFont(backendName)
    globalAxes = await font.getGlobalAxes()
    assert expectedGlobalAxes == globalAxes


getLibTestData = [
    ("designspace", 0),
    ("ufo", 17),
]


@pytest.mark.asyncio
@pytest.mark.parametrize("backendName, expectedLibLen", getLibTestData)
async def test_getFontLib(backendName, expectedLibLen):
    font = getTestFont(backendName)
    lib = await font.getFontLib()
    assert expectedLibLen == len(lib)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "backendName, expectedUnitsPerEm",
    [
        ("designspace", 1000),
        ("ufo", 1000),
        ("ttf", 1000),
    ],
)
async def test_getUnitsPerEm(backendName, expectedUnitsPerEm):
    font = getTestFont(backendName)
    unitsPerEm = await font.getUnitsPerEm()
    assert expectedUnitsPerEm == unitsPerEm
