from unittest import TestCase
from unittest.mock import create_autospec

import torch
from torch import nn

from torchft.ddp import DistributedDataParallel
from torchft.manager import Manager


class TestDDP(TestCase):
    def test_ddp(self):
        manager = create_autospec(Manager)

        m = nn.Linear(3, 4)
        m = DistributedDataParallel(m, manager)

        inp = torch.rand(2, 3)
        out = m(inp)
        loss = out.mean()
        loss.backward()

        for p in m.parameters():
            self.assertIsNotNone(p.grad)
