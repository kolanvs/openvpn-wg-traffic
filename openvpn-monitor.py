from lib.config_loader import ConfigLoader
from lib.utilites import get_args
from lib.openvpn_management import OpenvpnMgmtInterface

def main(**kwargs):
    print("Lol Kek Cheburek")
    cfg = ConfigLoader(args.config)
    print(cfg.settings)
    print(cfg.vpns)
    monitor = OpenvpnMgmtInterface(cfg, **kwargs)
    # if args.debug:
    #     pretty_vpns = pformat((dict(monitor.vpns)))
    #     debug("=== begin vpns\n{0!s}\n=== end vpns".format(pretty_vpns))


if __name__ == '__main__':
    args = get_args()
    wsgi = False
    main()
