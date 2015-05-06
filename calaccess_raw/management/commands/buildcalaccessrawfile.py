from optparse import make_option
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_model_list


custom_options = (
    make_option(
        "--skip-download",
        action="store_true",
        dest="skip_download",
        default=False,
        help="Skip downloading of the ZIP archive"
    ),
    make_option(
        "--only-download",
        action="store_true",
        dest="only_download",
        default=False,
        help="Only download the ZIP archive"
    ),
    make_option(
        "--skip-unzip",
        action="store_true",
        dest="skip_unzip",
        default=False,
        help="Skip unzipping of the archive"
    ),
    make_option(
        "--only-unzip",
        action="store_true",
        dest="only_unzip",
        default=False,
        help="Only unzip the archive"
    ),
    make_option(
        "--skip-prep",
        action="store_true",
        dest="skip_prep",
        default=False,
        help="Skip prepping of the unzipped archive"
    ),
    make_option(
        "--only-prep",
        action="store_true",
        dest="only_prep",
        default=False,
        help="Only prep the unzipped archive"
    ),
    make_option(
        "--skip-clear",
        action="store_true",
        dest="skip_clear",
        default=False,
        help="Skip clearing out ZIP archive and extra files"
    ),
    make_option(
        "--only-clear",
        action="store_true",
        dest="only_clear",
        default=False,
        help="Only clear out ZIP archive and extra files"
    ),
    make_option(
        "--skip-clean",
        action="store_true",
        dest="skip_clean",
        default=False,
        help="Skip cleaning up the raw data files"
    ),
    make_option(
        "--only-clean",
        action="store_true",
        dest="only_clean",
        default=False,
        help="Only clean up the raw data files"
    ),
    make_option(
        "--skip-load",
        action="store_true",
        dest="skip_load",
        default=False,
        help="Skip loading up the raw data files"
    ),
    make_option(
        "--only-load",
        action="store_true",
        dest="only_load",
        default=False,
        help="Only load up the raw data files"
    ),
    make_option(
        "--noinput", "--quiet", "-q",
        action="store_true",
        dest="noinput",
        default=False,
        help="Download the ZIP archive without asking permission"
    ),
    make_option(
        "--use-test-data",
        action="store_true",
        dest="test_data",
        default=False,
        help="Use sampled test data (skips download, unzip, prep, clear)"
    ),
    make_option(
        "--only-tables",
        action="store",
        type="string",
        dest="only_tables"
    ),
)


# Takes flags for --skip and --only for the actions.
#
# You can one or more --only flags. If you use an --only flag,
# then --skip flags will be ignored.
#
# A --skip flag and an --only flag on the same action will
# cause an exception to be thrown.
#
class Command(CalAccessCommand):

    help = 'Download and process the data files from the CA SoS.'

    option_list = CalAccessCommand.option_list + custom_options

    def handle(self, *args, **options):

        toDos = []

        if options['skip_download'] and options['only_download']:
            raise Exception('bad options!')
        if options['skip_unzip'] and options['only_unzip']:
            raise Exception('bad options!')
        if options['skip_prep'] and options['only_prep']:
            raise Exception('bad options!')
        if options['skip_clear'] and options['only_clear']:
            raise Exception('bad options!')
        if options['skip_clean'] and options['only_clean']:
            raise Exception('bad options!')
        if options['skip_load'] and options['only_load']:
            raise Exception('bad options!')

        if options['only_download']:
            toDos.append('download')
        if options['only_unzip']:
            toDos.append('unzip')
        if options['only_prep']:
            toDos.append('prep')
        if options['only_clear']:
            toDos.append('clear')
        if options['only_clean']:
            toDos.append('clean')
        if options['only_load']:
            toDos.append('load')

        if len(toDos) == 0:
            toDos = ['download', 'unzip', 'prep', 'clear', 'clean', 'load']

            if options['skip_download']:
                toDos.remove('download')
            if options['skip_unzip']:
                toDos.remove('unzip')
            if options['skip_prep']:
                toDos.remove('prep')
            if options['skip_clear']:
                toDos.remove('clear')
            if options['skip_clean']:
                toDos.remove('clean')
            if options['skip_load']:
                toDos.remove('load')

        self.log('Ok')
        self.log('toDos: %s' % toDos)

        models = []
        for model in get_model_list():
            if model.__name__.endswith('Cd'):
                models.append(model.__name__)

        if options['only_tables'] is not None:
            only_set = set(options['only_tables'].split(','))
            models = list(only_set.intersection(set(models)))

        msg = 'Please provide a comma-separated list of tables'
        msg = msg + ', such as "CvrSoCd,HdrCd"'

        if len(models) == 0:
            raise Exception(msg)

        self.log('model_list: %s' % models)

        # What Is to Be Done?
        #
        # download (in download)
        #
        # unzip (in download)
        #
        # prep (in download)
        #
        # clear (in download)
        #
        # clean (download calls command: cleancalaccessrawfile)
        #
        # load (download calls command: loadcalaccessrawfile)
        #
        # verify (optional, nobody calls it)
        #

