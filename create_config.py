import ConfigParser
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Description: create config for using gitlab tools'
        print 'Usage:'
        print '     ' + sys.argv[0] + ' <Gitlab URL> <Token>'
        sys.exit()
    url = sys.argv[1]
    token = sys.argv[2]

    config = ConfigParser.RawConfigParser()
    config.add_section('Auth')
    config.set('Auth', 'URL', url)
    config.set('Auth', 'Token', token)

    with open('auth.cfg', 'w+') as cfg:
        config.write(cfg) 
 
    print 'config created in auth.cfg'
    with open('auth.cfg', 'r') as cfg:
        print cfg.read()
