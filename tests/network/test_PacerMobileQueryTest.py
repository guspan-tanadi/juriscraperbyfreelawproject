#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

import unittest

from juriscraper.pacer.mobile_query import MobileQuery
from tests.network import SKIP_IF_NO_PACER_LOGIN, get_pacer_session


class PacerMobileQueryTest(unittest.TestCase):
    """A test of basic info for the Case Query"""

    def setUp(self):
        self.session = get_pacer_session()
        self.session.login()
        self.report = MobileQuery("cand", self.session)
        self.pacer_case_number = "4:06-cv-07294"  # Foley v. Bates

    @SKIP_IF_NO_PACER_LOGIN
    def test_query(self):
        self.report.query(self.pacer_case_number)

        # Can we get the docket entry count
        metadata = self.report.metadata
        if metadata["cost"]:
            print("we were charged. Details:", metadata["cost"])
        expected_de_count = 29
        actual_de_count = metadata["entry_count"]
        self.assertEqual(
            expected_de_count,
            actual_de_count,
            msg="entry_count query failed. Got %s; expected %s"
            % (actual_de_count, expected_de_count),
        )
        self.assertEqual(
            "", metadata["cost"], msg="cost query failed",
        )
