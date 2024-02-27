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

from pydantic import BaseModel, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ComplianceModelFields(BaseModel):
    """
    ComplianceModelFields
    """ # noqa: E501
    id: Optional[StrictInt] = None
    gpu_model: Optional[StrictStr] = None
    resource_type: Optional[StrictStr] = None
    base_value: Optional[StrictInt] = None
    variation_min: Optional[StrictInt] = None
    variation_max: Optional[StrictInt] = None
    variation_unit: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "gpu_model", "resource_type", "base_value", "variation_min", "variation_max", "variation_unit"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ComplianceModelFields from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ComplianceModelFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "gpu_model": obj.get("gpu_model"),
            "resource_type": obj.get("resource_type"),
            "base_value": obj.get("base_value"),
            "variation_min": obj.get("variation_min"),
            "variation_max": obj.get("variation_max"),
            "variation_unit": obj.get("variation_unit")
        })
        return _obj


