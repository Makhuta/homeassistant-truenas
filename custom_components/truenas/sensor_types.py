"""Definitions for TrueNAS sensor entities."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    UnitOfTemperature,
    UnitOfDataRate,
    UnitOfInformation,
)
from homeassistant.helpers.entity import EntityCategory

from .const import (
    SCHEMA_SERVICE_CLOUDSYNC_RUN,
    SCHEMA_SERVICE_DATASET_SNAPSHOT,
    SCHEMA_SERVICE_SYSTEM_REBOOT,
    SCHEMA_SERVICE_SYSTEM_SHUTDOWN,
    SERVICE_CLOUDSYNC_RUN,
    SERVICE_DATASET_SNAPSHOT,
    SERVICE_SYSTEM_REBOOT,
    SERVICE_SYSTEM_SHUTDOWN,
)

DEVICE_ATTRIBUTES_NETWORK = [
    "description",
    "mtu",
    "link_state",
    "active_media_type",
    "active_media_subtype",
    "link_address",
]

DEVICE_ATTRIBUTES_POOL = [
    "path",
    "status",
    "healthy",
    "is_decrypted",
    "autotrim",
    "scrub_state",
    "scrub_start",
    "scrub_end",
    "scrub_secs_left",
    "healthy",
    "total_gib",
]

DEVICE_ATTRIBUTES_DATASET = [
    "type",
    "pool",
    "mountpoint",
    "deduplication",
    "atime",
    "casesensitivity",
    "checksum",
    "exec",
    "sync",
    "compression",
    "compressratio",
    "quota",
    "copies",
    "readonly",
    "recordsize",
    "encryption_algorithm",
    "used",
    "available",
]

DEVICE_ATTRIBUTES_DISK = [
    "serial",
    "size",
    "hddstandby",
    "hddstandby_force",
    "advpowermgmt",
    "acousticlevel",
    "togglesmart",
    "model",
    "rotationrate",
    "type",
    "name",
    "devname",
    "zfs_guid",
    "identifier",
]

DEVICE_ATTRIBUTES_CPU = [
    "cpu_interrupt",
    "cpu_system",
    "cpu_user",
    "cpu_nice",
    "cpu_idle",
]

DEVICE_ATTRIBUTES_MEMORY = [
    "memory-used_value",
    "memory-free_value",
    "memory-cached_value",
    "memory-buffered_value",
    "memory-total_value",
]

DEVICE_ATTRIBUTES_CLOUDSYNC = [
    "direction",
    "path",
    "enabled",
    "transfer_mode",
    "snapshot",
    "time_started",
    "time_finished",
    "job_percent",
    "job_description",
]

DEVICE_ATTRIBUTES_REPLICATION = [
    "source_datasets",
    "target_dataset",
    "recursive",
    "enabled",
    "direction",
    "transport",
    "auto",
    "retention_policy",
    "state",
    "time_started",
    "time_finished",
    "job_percent",
    "job_description",
]

DEVICE_ATTRIBUTES_SNAPSHOTTASK = [
    "recursive",
    "lifetime_value",
    "lifetime_unit",
    "enabled",
    "naming_schema",
    "allow_empty",
    "vmware_sync",
    "state",
    "datetime",
]


@dataclass
class TrueNASSensorEntityDescription(SensorEntityDescription):
    """Class describing entities."""

    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    data_path: str | None = None
    data_attribute: str | None = None
    data_name: str | None = None
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "TrueNASSensor"


SENSOR_TYPES: tuple[TrueNASSensorEntityDescription, ...] = (
    TrueNASSensorEntityDescription(
        key="system_uptime",
        name="Uptime",
        icon="mdi:clock-outline",
        native_unit_of_measurement=None,
        device_class=SensorDeviceClass.TIMESTAMP,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="uptimeEpoch",
        data_name="",
        data_uid="",
        data_reference="",
        func="TrueNASUptimeSensor",
    ),
    TrueNASSensorEntityDescription(
        key="system_cpu_temperature",
        name="Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cpu_temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="system_load_shortterm",
        name="CPU load shortterm",
        icon="mdi:gauge",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="load_shortterm",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="system_load_midterm",
        name="CPU load midterm",
        icon="mdi:gauge",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="load_midterm",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="system_load_longterm",
        name="CPU load longterm",
        icon="mdi:gauge",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="load_longterm",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="system_cpu_usage",
        name="CPU usage",
        icon="mdi:cpu-64-bit",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cpu_usage",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_CPU,
    ),
    TrueNASSensorEntityDescription(
        key="system_memory_usage",
        name="Memory usage",
        icon="mdi:memory",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="memory-usage_percent",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_MEMORY,
    ),
    TrueNASSensorEntityDescription(
        key="system_cache_size-arc_value",
        name="ARC size",
        icon="mdi:memory",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_size-arc_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="system_cache_size-L2_value",
        name="L2ARC size",
        icon="mdi:memory",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_size-L2_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="system_cache_ratio-arc_value",
        name="ARC ratio",
        icon="mdi:aspect-ratio",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_ratio-arc_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="system_cache_ratio-L2_value",
        name="L2ARC ratio",
        icon="mdi:aspect-ratio",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="system_info",
        data_attribute="cache_ratio-L2_value",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    TrueNASSensorEntityDescription(
        key="dataset",
        name="",
        icon="mdi:database",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="Datasets",
        data_path="dataset",
        data_attribute="used_gb",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_DATASET,
        func="TrueNASDatasetSensor",
    ),
    TrueNASSensorEntityDescription(
        key="disk",
        name="",
        icon="mdi:harddisk",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="Disks",
        data_path="disk",
        data_attribute="temperature",
        data_name="identifier",
        data_uid="",
        data_reference="identifier",
        data_attributes_list=DEVICE_ATTRIBUTES_DISK,
    ),
    TrueNASSensorEntityDescription(
        key="pool_free",
        name="free",
        icon="mdi:database-settings",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="pool",
        data_attribute="available_gib",
        data_name="name",
        data_uid="",
        data_reference="guid",
        data_attributes_list=DEVICE_ATTRIBUTES_POOL,
    ),
    TrueNASSensorEntityDescription(
        key="cloudsync",
        name="",
        icon="mdi:cloud-upload",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Cloudsync",
        data_path="cloudsync",
        data_attribute="state",
        data_name="description",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_CLOUDSYNC,
        func="TrueNASClousyncSensor",
    ),
    TrueNASSensorEntityDescription(
        key="replication",
        name="",
        icon="mdi:transfer",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Replication",
        data_path="replication",
        data_attribute="state",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_REPLICATION,
    ),
    TrueNASSensorEntityDescription(
        key="snapshottask",
        name="",
        icon="mdi:checkbox-marked-circle-plus-outline",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Snapshot tasks",
        data_path="snapshottask",
        data_attribute="state",
        data_name="dataset",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_SNAPSHOTTASK,
    ),
    TrueNASSensorEntityDescription(
        key="traffic_rx",
        name="RX",
        icon="mdi:download-network-outline",
        native_unit_of_measurement=UnitOfDataRate.KIBIBYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.MEGABYTES_PER_SECOND,
        suggested_display_precision=2,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="interface",
        data_attribute="rx",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_NETWORK,
    ),
    TrueNASSensorEntityDescription(
        key="traffic_tx",
        name="TX",
        icon="mdi:upload-network-outline",
        native_unit_of_measurement=UnitOfDataRate.KIBIBYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.MEGABYTES_PER_SECOND,
        suggested_display_precision=2,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="interface",
        data_attribute="tx",
        data_name="name",
        data_uid="",
        data_reference="id",
        data_attributes_list=DEVICE_ATTRIBUTES_NETWORK,
    ),
)

SENSOR_SERVICES = [
    [SERVICE_CLOUDSYNC_RUN, SCHEMA_SERVICE_CLOUDSYNC_RUN, "start"],
    [SERVICE_DATASET_SNAPSHOT, SCHEMA_SERVICE_DATASET_SNAPSHOT, "snapshot"],
    [SERVICE_SYSTEM_REBOOT, SCHEMA_SERVICE_SYSTEM_REBOOT, "restart"],
    [SERVICE_SYSTEM_SHUTDOWN, SCHEMA_SERVICE_SYSTEM_SHUTDOWN, "stop"],
]
