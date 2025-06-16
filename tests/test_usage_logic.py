import pytest
from unittest.mock import patch, AsyncMock
from src.orbital_usage_api.usage_logic import compute_usage_report
from src.orbital_usage_api.models import UsageResponse

@pytest.mark.asyncio
async def test_usage_with_valid_report():
  # mock_messages and mock_report will be the Mocked Responses
  # for the `patch` function used to Mock.
  mock_messages = [
    {
      "id": 1001,
      "timestamp": "2024-06-01T10:00:00Z",
      "text": "Generate a Test Legal Report",
      "report_id": "5392"
    }
  ]

  mock_report = {
    "id": "5392",
    "name": "Unit Test Report",
    "credit_cost": 42.5
  }

  # we need to Mock the internal HTTP calls in the data layer to make the Unit Tests Manageable
  # and fast
  with patch("src.orbital_usage_api.usage_logic.fetch_messages", new = AsyncMock(return_value = mock_messages)), \
       patch("src.orbital_usage_api.usage_logic.fetch_report", new = AsyncMock(return_value = mock_report)):

    result = await compute_usage_report()
    assert isinstance(result, UsageResponse)
    assert len(result.usage) == 1

    record = result.usage[0]
    assert record.message_id == 1001
    assert record.timestamp == "2024-06-01T10:00:00Z"
    assert record.report_name == "Unit Test Report"
    assert record.credits_used == 42.5

@pytest.mark.asyncio
async def test_usage_with_invalid_report():
  mock_messages = [
    {
      "id": 1002,
      "timestamp": "2024-06-02T11:00:00Z",
      "text": "What are the indemnity provisions?",
      "report_id": "1124"
    }
  ]

  with patch("src.orbital_usage_api.usage_logic.fetch_messages", new = AsyncMock(return_value = mock_messages)), \
       patch("src.orbital_usage_api.usage_logic.fetch_report", new = AsyncMock(return_value = None)), \
       patch("src.orbital_usage_api.usage_logic.calculate_credits", return_value = 5.55):

    result = await compute_usage_report()
    record = result.usage[0]

    assert record.message_id == 1002
    assert record.report_name is None
    assert record.credits_used == 5.55

@pytest.mark.asyncio
async def test_usage_without_report_id():
  mock_messages = [
    {
      "id": 1003,
      "timestamp": "2024-06-03T12:00:00Z",
      "text": "Are there any clauses for dispute resolution?"
    }
  ]

  with patch("src.orbital_usage_api.usage_logic.fetch_messages", new = AsyncMock(return_value = mock_messages)), \
       patch("src.orbital_usage_api.usage_logic.calculate_credits", return_value = 3.33):

    result = await compute_usage_report()
    record = result.usage[0]

    assert record.message_id == 1003
    assert record.report_name is None
    assert record.credits_used == 3.33
