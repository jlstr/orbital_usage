import pytest
from pydantic import ValidationError
from src.orbital_usage_api.models import UsageRecord, UsageResponse

def test_valid_usage_record():
  record = UsageRecord(
    message_id = 1234,
    timestamp = "2024-06-13T12:00:00Z",
    report_name = "Compliance Report",
    credits_used = 10.5
  )

  assert record.message_id == 1234
  assert record.timestamp == "2024-06-13T12:00:00Z"
  assert record.report_name == "Compliance Report"
  assert record.credits_used == 10.5

def test_usage_record_without_optional_report_name():
  record = UsageRecord(
    message_id = 5447,
    timestamp = "2024-06-13T12:30:00Z",
    credits_used = 5.0
  )

  assert record.report_name is None

def test_invalid_message_id_type():
  # Checking if the exception raised, captured in `validation`
  # contains the substring "message_id"
  with pytest.raises(ValidationError) as validation:
    UsageRecord(
      message_id = "abcd",  # Should be a number!
      timestamp = "2024-06-13T12:00:00Z",
      credits_used = 1.0
    )

  assert "message_id" in str(validation.value)

def test_valid_usage_response_with_multiple_records():
  records = [
    UsageRecord(
      message_id = 1,
      timestamp = "2024-06-13T12:00:00Z",
      credits_used = 5.0
    ),
    UsageRecord(
      message_id = 2,
      timestamp = "2024-06-13T12:10:00Z",
      report_name = "Summary",
      credits_used = 7.5
    )
  ]

  response = UsageResponse(usage = records)

  assert isinstance(response.usage, list)
  assert len(response.usage) == 2
  assert response.usage[1].report_name == "Summary"

def test_invalid_usage_response_structure():
  # Means it will raise an Exception with a message that contains the
  # substring "message_id" in it
  with pytest.raises(ValidationError) as validation:
    UsageResponse(usage = [
      {
        "id": 1234,
        "timestamp": "2024-06-13T13:00:00Z",
        "credits_used": 3.0
      }
    ])

  assert "message_id" in str(validation.value)