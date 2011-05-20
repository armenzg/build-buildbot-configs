# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'accessibility': {
        'enable_nightly': True,
        'enable_mobile': False,
        'mobile_platforms': {},
        # only want a11y so turn off the default set
        'talos_suites': {
            'dirty': 0,
            'tp4': 0,
            'chrome': 0,
            'nochrome': 0,
            'dromaeo': 0,
            'svg': 0,
            'scroll': 0,
            'paint': 0,
        },
    },
    'build-system': {
        'enable_talos': False,
    },
    'devtools':{
        'enable_nightly': True,
        # need both of these to turn off mobile completely because of key in generic config.py
        'enable_mobile': False,
        'mobile_platforms': {},
        'platforms': {
            'macosx-debug': {
                'dont_build': True,
            },
            'macosx': {
                'slave_platforms': [],
            },
            'macosx64': {
                'slave_platforms': ['snowleopard'],
            },
            'android': {
                'tegra_android': {},
            },
        },
    },
    'electrolysis': {
        'mozconfig_dir': 'electrolysis',
        'mobile_platforms': {
            'maemo5-gtk': {
                'mozconfig': 'mobile/maemo5-gtk/mobile-e10s/nightly',
            },
            'maemo5-qt': {
                'mozconfig': 'mobile/maemo5-qt/mobile-e10s/nightly',
            },
            'linux': {
                'mozconfig': 'mobile/linux-i686/mobile-e10s/nightly',
            },
            'win32': {
                'mozconfig': 'mobile/win32-i686/mobile-e10s/nightly',
            },
            'macosx': {
                'mozconfig': 'mobile/macosx-i686/mobile-e10s/nightly',
            },
            'android-r7': {},
        },
        'enable_talos': False,
    },
    'graphics':{
        'enable_unittests': False,
        'enable_talos': False,
    },
    'jaegermonkey': {
        'enable_talos': False,
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
    },
    'places': {
        'platforms': {
            'linux64': {
                'build_space': 6,
            },
            'linux': {
                'build_space': 6,
            },
            'linuxqt': { 
                'build_space': 6,
            },
        },
        'talos_suites': {
            'remote-ts': 1,
            'remote-tdhtml': 1,
            'remote-tsvg': 1,
            'remote-tsspider': 1,
            'remote-twinopen': 1,
        }
    },
    'private-browsing': {
        'enable_talos': False,
        'enable_mobile': False,
        'mobile_platforms': {},
        'enable_nightly': True,
    },
    'services-central': {
        'repo_path': 'services/services-central',
        'enable_weekly_bundle': True,
    },
    'tracemonkey': {
        'repo_path': 'tracemonkey',
        'mozconfig_dir': 'tracemonkey',
        'branch_name': 'TraceMonkey',
        'mobile_branch_name': 'TraceMonkey',
        'build_branch': 'TraceMonkey',
        'start_hour': [3],
        'start_minute': [32],
        'enable_nightly': True,
        'enable_mobile_nightly': True,
        'enable_shark': True,
        'platforms': {
            'linux64': {
                'build_space': 7,
            },
            'linux': {
                'build_space': 7,
            },
            'linuxqt': { 
                'build_space': 7,
            },
            'linux-debug': {
                'enable_valgrind_checktests': True,
            },
            'linux64-debug': {
                'enable_valgrind_checktests': True,
            },
        }, 
        'create_snippet': True,
        'create_partial': True,
        'talos_suites': {
            'remote-ts': 1,
            'remote-tdhtml': 1,
            'remote-tsvg': 1,
            'remote-tsspider': 1,
            'remote-tpan': 1,
            'v8': 1,
        }
    },
    'ux': {
        'branch_name': 'UX',
        'mobile_branch_name': 'UX',
        'build_branch': 'UX',
        'tinderbox_tree': 'UX',
        'mobile_tinderbox_tree': 'UX',
        'packaged_unittest_tinderbox_tree': 'UX',
        'enable_mobile': False,
        'mobile_platforms': {},
        'mozconfig_dir' : 'ux',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'platforms': {
            'macosx-debug': {
                'dont_build': True,
            },
            'macosx64-debug': {
                'dont_build': True,
            },
            'linux-debug': {
                'dont_build': True,
            },
            'linux64-debug': {
                'dont_build': True,
            },
            'win32-debug': {
                'dont_build': True,
            },
        },
    },
    #####  TWIGS aka RENTABLE BRANCHES
    'alder': {},
    'birch': {
        'platforms': {
            'macosx': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
            },
            'macosx-debug': {
                'dont_build': True,
            },
            'macosx64': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
            },
            'macosx64-debug': {
                'dont_build': True,
            },
            'linux': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
            },
            'linux-debug': {
                'dont_build': True,
            },
            'linux64': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
            },
            'linux64-debug': {
                'dont_build': True,
            },
            'win32': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
            },
            'win32-debug': {
                'dont_build': True,
            },
        },
    },
    'cedar': {
        # Share mozilla-central's setup as much as possible
        'mozconfig_dir' : 'mozilla-central',
        'talos_suites': {
            'remote-ts': 1,
            'remote-tdhtml': 1,
            'remote-tsvg': 1,
            'remote-tsspider': 1,
            'remote-twinopen': 1,
        }
    },
    'holly': {},
    'larch': {},
    'maple': {},
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()
# Turning off graphics - bug 649507
for branch in ('graphics',):
    ACTIVE_PROJECT_BRANCHES.remove(branch)

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = PROJECT_BRANCHES[branch].get('tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('mobile_tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('packaged_unittest_tinderbox_tree', branch.title())
