import shutil
from pathlib import Path

import pytest

from subtotal import subtotal

root = Path(__file__).parent


def test__subtotal__get_args():
    ...


def test__subtotal__expand_subdomains():
    ...


def test__subtotal__get_subdomains():
    ...


class MockArgs:
    def __init__(self, url: str):
        self.url = url
        self.browser = "firefox"
        self.output_file = root / "subtotals" / f"tryhackme.com-subdomains.txt"
        self.output_file.parent.mkdir(parents=True, exist_ok=True)


@pytest.mark.parametrize("url", ["tryhackme.com", "https://tryhackme.com/"])
def test__subtotal__main(url: str):
    args = MockArgs(url)
    subtotal.main(args)
    control = (root / "tryhackme_domains.txt").read_text().splitlines()
    test = (args.output_file).read_text().splitlines()
    assert len(test) == len(control)
    for subdomain in test:
        assert subdomain in control
    shutil.rmtree(args.output_file.parent)
