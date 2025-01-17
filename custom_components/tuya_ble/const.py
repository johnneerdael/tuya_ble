"""The Tuya BLE integration."""
from __future__ import annotations

from enum import StrEnum
from typing_extensions import Final

DOMAIN: Final = "tuya_ble"

# Configuration constants
CONF_ACCESS_ID: Final = "access_id"
CONF_ACCESS_SECRET: Final = "access_secret"
CONF_USERNAME: Final = "username"
CONF_PASSWORD: Final = "password"
CONF_COUNTRY_CODE: Final = "country_code"
CONF_ENDPOINT: Final = "endpoint"
CONF_APP_TYPE: Final = "app_type"
CONF_AUTH_TYPE: Final = "auth_type"

# App types
TUYA_SMART_APP: Final = "tuyaSmart"
SMARTLIFE_APP: Final = "smartlife"

# Response constants
TUYA_RESPONSE_SUCCESS: Final = "success"
TUYA_RESPONSE_CODE: Final = "code"
TUYA_RESPONSE_MSG: Final = "msg"
TUYA_RESPONSE_RESULT: Final = "result"

# Domain of main Tuya integration
TUYA_DOMAIN: Final = "tuya"

# Device metadata
DEVICE_METADATA_UUIDS: Final = "uuids"
DEVICE_DEF_MANUFACTURER: Final = "Tuya"
SET_DISCONNECTED_DELAY = 10 * 60

# Device configuration
CONF_UUID: Final = "uuid"
CONF_LOCAL_KEY: Final = "local_key"
CONF_CATEGORY: Final = "category"
CONF_PRODUCT_ID: Final = "product_id"
CONF_DEVICE_NAME: Final = "device_name"
CONF_PRODUCT_MODEL: Final = "product_model"
CONF_PRODUCT_NAME: Final = "product_name"

# API endpoints
TUYA_API_DEVICES_URL: Final = "/v1.0/users/%s/devices"
TUYA_API_FACTORY_INFO_URL: Final = "/v1.0/iot-03/devices/factory-infos?device_ids=%s"
TUYA_FACTORY_INFO_MAC: Final = "mac"

# Battery states
BATTERY_STATE_LOW: Final = "low"
BATTERY_STATE_NORMAL: Final = "normal"
BATTERY_STATE_HIGH: Final = "high"

# Battery charging states
BATTERY_NOT_CHARGING: Final = "not_charging"
BATTERY_CHARGING: Final = "charging"
BATTERY_CHARGED: Final = "charged"

# CO2 levels
CO2_LEVEL_NORMAL: Final = "normal"
CO2_LEVEL_ALARM: Final = "alarm"

# Fingerbot modes
FINGERBOT_MODE_PUSH: Final = "push"
FINGERBOT_MODE_SWITCH: Final = "switch"
FINGERBOT_MODE_PROGRAM: Final = "program"
FINGERBOT_BUTTON_EVENT: Final = "fingerbot_button_pressed"

