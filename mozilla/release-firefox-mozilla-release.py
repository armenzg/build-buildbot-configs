# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
releaseConfig = {}
releaseConfig['base_clobber_url'] = 'https://api.pub.build.mozilla.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = ['<release-automation-notifications@mozilla.com>',]
releaseConfig['ImportantRecipients'] = ['<release-drivers@mozilla.org>',]
releaseConfig['AVVendorsRecipients'] = ['<av-vendor-release-announce@mozilla.org>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['stage_product']       = 'firefox'
releaseConfig['appName']             = 'browser'
#  Current version info
releaseConfig['version']             = '43.0.4'
releaseConfig['appVersion']          = '43.0.4'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_43_0_4'
releaseConfig['partialUpdates']      = {

    '43.0.1': {
        'appVersion': '43.0.1',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_43_0_1',
    },

    '43.0.3': {
        'appVersion': '43.0.3',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_43_0_3',
    },

    '43.0.2': {
        'appVersion': '43.0.2',
        'buildNumber': 1,
        'baseTag': 'FIREFOX_43_0_2',
    },

}
# What's New Page, should be revisited with each release.
# releaseConfig['openURL'] = 'https://www.mozilla.org/%LOCALE%/firefox/43.0.4/whatsnew/?oldversion=%OLD_VERSION%'

releaseConfig['HACK_first_released_version'] = {'win64': "42.0"}

#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-release',
        'path': 'releases/mozilla-release',
        'revision': '413d833d300a',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'browser/config/version_display.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n/mozilla-release'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-release'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64', "win64")
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = False

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_rsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'archive.mozilla.org'
releaseConfig['stagingServer']       = 'upload.ffxbld.productdelivery.prod.mozaws.net'
releaseConfig['S3Credentials']       = '/builds/release-s3.credentials'
releaseConfig['S3Bucket']            = 'net-mozaws-prod-delivery-firefox'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus4.mozilla.org'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['updateVerifyChunks']  = 6
releaseConfig['mozconfigs']          = {
    'linux': 'browser/config/mozconfigs/linux32/release',
    'linux64': 'browser/config/mozconfigs/linux64/release',
    'macosx64': 'browser/config/mozconfigs/macosx-universal/release',
    'win32': 'browser/config/mozconfigs/win32/release',
    'win64': 'browser/config/mozconfigs/win64/release',
}
releaseConfig["releaseChannel"] = "release"
releaseConfig['updateChannels'] = {
    "release": {
        "versionRegex": r"^\d+\.\d+(\.\d+)?$",
        "ruleId": 145,
        "patcherConfig": "mozRelease-branch-patcher2.cfg",
        "localTestChannel": "release-localtest",
        "cdnTestChannel": "release-cdntest",
        "verifyConfigs": {
            "linux":  "mozRelease-firefox-linux.cfg",
            "linux64":  "mozRelease-firefox-linux64.cfg",
            "macosx64": "mozRelease-firefox-mac64.cfg",
            "win32":  "mozRelease-firefox-win32.cfg",
            "win64":  "mozRelease-firefox-win64.cfg",
        },
        "testChannels": {
            "release-localtest": {
                "ruleId": 56,
            },
            "release-cdntest": {
                "ruleId": 57,
            },
        },
    },
    "beta": {
        "enabled": False,
        # For the beta channel, we want to able to provide updates to this
        # from prior betas or prior RCs that were shipped to the beta channel,
        # so this regex matches either.
        "versionRegex": r"^(\d+\.\d+(b\d+)?)$",
        "ruleId": 32,
        "requiresMirrors": False,
        "patcherConfig": "mozBeta-branch-patcher2.cfg",
        "localTestChannel": "beta-localtest",
        "cdnTestChannel": "beta-cdntest",
        "verifyConfigs": {
            "linux":  "mozBeta-firefox-linux.cfg",
            "linux64":  "mozBeta-firefox-linux64.cfg",
            "macosx64": "mozBeta-firefox-mac64.cfg",
            "win32":  "mozBeta-firefox-win32.cfg",
            "win64":  "mozBeta-firefox-win64.cfg",
        },
        "marChannelIds": [
            "firefox-mozilla-beta",
            "firefox-mozilla-release",
        ],
        "testChannels": {
            "beta-cdntest": {
                "ruleId": 45,
            },
            "beta-localtest": {
                "ruleId": 25,
            },
        }
    }
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'
releaseConfig['syncPartnerBundles']  = False

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_firefox_release.py'

# Product details config
releaseConfig["productDetailsRepo"] = "svn+ssh://ffxbld@svn.mozilla.org/libs/product-details"
releaseConfig["mozillaComRepo"]     = "svn+ssh://ffxbld@svn.mozilla.org/projects/mozilla.com"
releaseConfig["svnSshKey"]          = "/home/cltbld/.ssh/ffxbld_rsa"

# Misc configuration
releaseConfig['makeIndexFiles'] = True
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['ftpSymlinkName'] = 'latest'

releaseConfig['bouncer_aliases'] = {
    'Firefox-%(version)s': 'firefox-latest',
    'Firefox-%(version)s-stub': 'firefox-stub',
}