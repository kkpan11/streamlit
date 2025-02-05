# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2025)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

import pytest
from playwright.sync_api import Page, expect

from e2e_playwright.conftest import ImageCompareFunction


@pytest.fixture(scope="module")
@pytest.mark.early
def configure_snowflake_light_theme():
    """Configure snowflake theme."""
    os.environ["STREAMLIT_THEME_BASE"] = "light"
    os.environ["STREAMLIT_THEME_PRIMARY_COLOR"] = "#1a6ce7"
    os.environ["STREAMLIT_THEME_BACKGROUND_COLOR"] = "#ffffff"
    os.environ["STREAMLIT_THEME_SECONDARY_BACKGROUND_COLOR"] = "#f7f7f7"
    os.environ["STREAMLIT_THEME_TEXT_COLOR"] = "#1e252f"
    os.environ["STREAMLIT_THEME_BORDER_COLOR"] = "#d5dae4"
    os.environ["STREAMLIT_THEME_SHOW_BORDER_AROUND_INPUTS"] = "True"
    os.environ["STREAMLIT_CLIENT_TOOLBAR_MODE"] = "minimal"
    # Todo: add bodyFont, codeFont & fontFaces
    yield
    del os.environ["STREAMLIT_THEME_BASE"]
    del os.environ["STREAMLIT_THEME_PRIMARY_COLOR"]
    del os.environ["STREAMLIT_THEME_BACKGROUND_COLOR"]
    del os.environ["STREAMLIT_THEME_SECONDARY_BACKGROUND_COLOR"]
    del os.environ["STREAMLIT_THEME_TEXT_COLOR"]
    del os.environ["STREAMLIT_THEME_BORDER_COLOR"]
    del os.environ["STREAMLIT_THEME_SHOW_BORDER_AROUND_INPUTS"]
    del os.environ["STREAMLIT_CLIENT_TOOLBAR_MODE"]


def test_snowflake_light_theme(
    app: Page, assert_snapshot: ImageCompareFunction, configure_snowflake_light_theme
):
    # Make sure that all elements are rendered and no skeletons are shown:
    expect(app.get_by_test_id("stSkeleton")).to_have_count(0, timeout=25000)
    assert_snapshot(app, name="snowflake_light_theme")
