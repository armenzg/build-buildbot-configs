from buildbot.steps.shell import WithProperties

GRAPH_CONFIG = ['--resultsServer', 'graphs-stage.mozilla.org', '--resultsLink', '/server/collect.cgi']

TALOS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:tdhtml:twinopen:tsspider:tgfx']

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_JSS_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tjss']

TALOS_DIRTY_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:ts_places_generated_min:ts_places_generated_med:ts_places_generated_max']
TALOS_DIRTY_ADDONS = ['/builds/buildbot/profiles/dirtyDBs.zip', '/builds/buildbot/profiles/dirtyMaxDBs.zip']

TALOS_TP4_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tp4']

TALOS_COLD_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'ts:ts_cold']

TALOS_SVG_CONFIG_OPTIONS = GRAPH_CONFIG + ['--activeTests', 'tsvg:tsvg_opacity']

SLAVES = {
    'linux': ["qm-pubuntu-try%02i" % x for x in range(1,12)],
    'xp': ["qm-pxp-try%02i" % x for x in range(1,11)],
    'vista': ["qm-pvista-try%02i" % x for x in range(1,12)],
    'tiger': ["qm-ptiger-try%02i" % x for x in range(1,3)],
    'leopard': ["qm-pleopard-try%02i" % x for x in range(1,12)],
}

PLATFORMS = {
    'macosx': {},
    'win32': {},
    'linux': {},
}

PLATFORMS['macosx']['slave_platforms'] = ['tiger', 'leopard']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['tiger'] = {'name': "MacOSX Darwin 8.8.1"}
PLATFORMS['macosx']['leopard'] = {'name': "MacOSX Darwin 9.0.0"}

PLATFORMS['win32']['slave_platforms'] = ['xp', 'vista']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "WINNT 5.1"}
PLATFORMS['win32']['vista'] = {'name': "WINNT 6.0"}

PLATFORMS['linux']['slave_platforms'] = ['linux']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['linux'] = {'name': "Linux"}

NO_WIN = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['macosx']['slave_platforms']
