from invoke import Collection
from musher import build
from musher import clean
from musher import deps
from musher import deploy
from musher import test

ns = Collection()
ns.add_collection(build)
ns.add_collection(clean)
ns.add_collection(deps)
ns.add_collection(deploy)
ns.add_collection(test)
