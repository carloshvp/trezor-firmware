from trezor import wire
from trezor.messages.GetState import GetState
from trezor.messages.State import State

from apps.common import cache
from apps.common.request_passphrase import protect_by_passphrase


async def get_state(ctx: wire.Context, msg: GetState) -> State:
    passphrase = await protect_by_passphrase(ctx)
    state = cache.get_state(passphrase=passphrase)  # TODO: prev_state ?
    return State(state)
