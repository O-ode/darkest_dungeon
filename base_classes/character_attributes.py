import warnings

from base_classes.basic_attribute import BasicAttribute

warnings.warn("File to be updated", DeprecationWarning)


class Tag(BasicAttribute):
    pass


class HP(BasicAttribute):
    pass


class Dodge(BasicAttribute):
    pass


class Prot(BasicAttribute):
    pass


class Spd(BasicAttribute):
    pass


class Crit(BasicAttribute):
    pass


class AccMod(BasicAttribute):
    pass
