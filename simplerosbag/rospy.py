# rospy.logwarn(
#    'Failed to load Python extension for LZ4 support. '
#    'LZ4 compression will not be available.')

def logwarn(msg, *args, **kwargs):
    print(msg)
    print("\n".join(args))

# rospy.Time(*struct.unpack('<LL', v))
from .rostime import Time # , Duration, get_rostime, get_time
