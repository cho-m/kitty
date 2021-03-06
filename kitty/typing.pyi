from asyncio import AbstractEventLoop as AbstractEventLoop
from socket import AddressFamily as AddressFamily, socket as Socket
from subprocess import (
    CompletedProcess as CompletedProcess, Popen as PopenType
)
from typing import (
    Literal, Protocol as Protocol, TypedDict as TypedDict
)

from kittens.hints.main import Mark as MarkType
from kittens.tui.handler import Handler as HandlerType
from kittens.tui.images import (
    GraphicsCommand as GraphicsCommandType, ImageManager as ImageManagerType
)
from kittens.tui.loop import (
    Debug as Debug, Loop as LoopType, MouseEvent as MouseEvent,
    TermManager as TermManagerType
)
from kitty.conf.utils import KittensKeyAction as KittensKeyActionType

from .boss import Boss as BossType
from .child import Child as ChildType
from .conf.utils import BadLine as BadLineType
from .config import (
    KeyAction as KeyActionType, KeyMap as KeyMap,
    KittyCommonOpts as KittyCommonOpts, SequenceMap as SequenceMap
)
from .fast_data_types import (
    CoreTextFont as CoreTextFont, FontConfigPattern as FontConfigPattern,
    Screen as ScreenType, StartupCtx as StartupCtx
)
from .key_encoding import KeyEvent as KeyEventType
from .layout.base import Layout as LayoutType
from .rc.base import RemoteCommand as RemoteCommandType
from .session import Session as SessionType, Tab as SessionTab
from .tabs import (
    SpecialWindowInstance as SpecialWindowInstance, Tab as TabType
)
from .utils import ScreenSize as ScreenSize
from .window import Window as WindowType

EdgeLiteral = Literal['left', 'top', 'right', 'bottom']
MatchType = Literal['mime', 'ext', 'protocol', 'file', 'path', 'url', 'fragment_matches']
GRT_a = Literal['t', 'T', 'q', 'p', 'd']
GRT_f = Literal[24, 32, 100]
GRT_t = Literal['d', 'f', 't', 's']
GRT_o = Literal['z']
GRT_m = Literal[0, 1]
GRT_d = Literal['a', 'A', 'c', 'C', 'i', 'I', 'p', 'P', 'q', 'Q', 'x', 'X', 'y', 'Y', 'z', 'Z']
__all__ = (
    'EdgeLiteral', 'MatchType', 'GRT_a', 'GRT_f', 'GRT_t', 'GRT_o', 'GRT_m', 'GRT_d',
    'GraphicsCommandType', 'HandlerType', 'AbstractEventLoop', 'AddressFamily', 'Socket', 'CompletedProcess',
    'PopenType', 'Protocol', 'TypedDict', 'MarkType', 'ImageManagerType', 'Debug', 'LoopType', 'MouseEvent',
    'TermManagerType', 'KittensKeyActionType', 'BossType', 'ChildType', 'BadLineType',
    'KeyActionType', 'KeyMap', 'KittyCommonOpts', 'SequenceMap', 'CoreTextFont',
    'FontConfigPattern', 'ScreenType', 'StartupCtx', 'KeyEventType', 'LayoutType',
    'RemoteCommandType', 'SessionType', 'SessionTab', 'SpecialWindowInstance', 'TabType', 'ScreenSize', 'WindowType'
)
