# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hyperstack.models.instance_environment_fields import InstanceEnvironmentFields
from hyperstack.models.instance_flavor_fields import InstanceFlavorFields
from hyperstack.models.instance_image_fields import InstanceImageFields
from hyperstack.models.instance_keypair_fields import InstanceKeypairFields
from hyperstack.models.security_rules_fieldsfor_instance import SecurityRulesFieldsforInstance
from hyperstack.models.volume_attachment_fields import VolumeAttachmentFields
from typing import Optional, Set
from typing_extensions import Self

class InstanceFields(BaseModel):
    """
    InstanceFields
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    environment: Optional[InstanceEnvironmentFields] = None
    image: Optional[InstanceImageFields] = None
    flavor: Optional[InstanceFlavorFields] = None
    os: Optional[StrictStr] = None
    keypair: Optional[InstanceKeypairFields] = None
    volume_attachments: Optional[List[VolumeAttachmentFields]] = None
    security_rules: Optional[List[SecurityRulesFieldsforInstance]] = None
    power_state: Optional[StrictStr] = None
    vm_state: Optional[StrictStr] = None
    fixed_ip: Optional[StrictStr] = None
    floating_ip: Optional[StrictStr] = None
    floating_ip_status: Optional[StrictStr] = None
    locked: Optional[StrictBool] = None
    contract_id: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    labels: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "status", "environment", "image", "flavor", "os", "keypair", "volume_attachments", "security_rules", "power_state", "vm_state", "fixed_ip", "floating_ip", "floating_ip_status", "locked", "contract_id", "created_at", "labels"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InstanceFields from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flavor
        if self.flavor:
            _dict['flavor'] = self.flavor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keypair
        if self.keypair:
            _dict['keypair'] = self.keypair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volume_attachments (list)
        _items = []
        if self.volume_attachments:
            for _item in self.volume_attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volume_attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in security_rules (list)
        _items = []
        if self.security_rules:
            for _item in self.security_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['security_rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InstanceFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "environment": InstanceEnvironmentFields.from_dict(obj["environment"]) if obj.get("environment") is not None else None,
            "image": InstanceImageFields.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "flavor": InstanceFlavorFields.from_dict(obj["flavor"]) if obj.get("flavor") is not None else None,
            "os": obj.get("os"),
            "keypair": InstanceKeypairFields.from_dict(obj["keypair"]) if obj.get("keypair") is not None else None,
            "volume_attachments": [VolumeAttachmentFields.from_dict(_item) for _item in obj["volume_attachments"]] if obj.get("volume_attachments") is not None else None,
            "security_rules": [SecurityRulesFieldsforInstance.from_dict(_item) for _item in obj["security_rules"]] if obj.get("security_rules") is not None else None,
            "power_state": obj.get("power_state"),
            "vm_state": obj.get("vm_state"),
            "fixed_ip": obj.get("fixed_ip"),
            "floating_ip": obj.get("floating_ip"),
            "floating_ip_status": obj.get("floating_ip_status"),
            "locked": obj.get("locked"),
            "contract_id": obj.get("contract_id"),
            "created_at": obj.get("created_at"),
            "labels": obj.get("labels")
        })
        return _obj

