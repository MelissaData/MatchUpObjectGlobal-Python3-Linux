from ctypes import *
from enum import Enum
import ctypes
import os
import sys

if (os.name == 'nt' and sys.version_info[:2] >= (3,8)):
  lib = ctypes.CDLL('mdMatchup.dll', winmode=0)
elif (os.name == 'nt'):
  lib = ctypes.CDLL('mdMatchup.dll')
else:
  lib = ctypes.CDLL('libmdMatchup.so')

lib.mdMUMatchcodeComponentCreate.argtypes = []
lib.mdMUMatchcodeComponentCreate.restype = c_void_p
lib.mdMUMatchcodeComponentDestroy.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentDestroy.restype = None
lib.mdMUMatchcodeComponentGetComponentType.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetComponentType.restype = c_int
lib.mdMUMatchcodeComponentSetComponentType.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetComponentType.restype = None
lib.mdMUMatchcodeComponentGetSize.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetSize.restype = c_int
lib.mdMUMatchcodeComponentSetSize.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetSize.restype = None
lib.mdMUMatchcodeComponentGetLabel.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetLabel.restype = c_char_p
lib.mdMUMatchcodeComponentSetLabel.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentSetLabel.restype = None
lib.mdMUMatchcodeComponentGetWordCount.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetWordCount.restype = c_int
lib.mdMUMatchcodeComponentSetWordCount.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetWordCount.restype = None
lib.mdMUMatchcodeComponentGetStart.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetStart.restype = c_int
lib.mdMUMatchcodeComponentSetStart.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetStart.restype = None
lib.mdMUMatchcodeComponentGetStartPos.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetStartPos.restype = c_int
lib.mdMUMatchcodeComponentSetStartPos.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetStartPos.restype = None
lib.mdMUMatchcodeComponentGetTrim.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetTrim.restype = c_int
lib.mdMUMatchcodeComponentSetTrim.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetTrim.restype = None
lib.mdMUMatchcodeComponentGetFuzzy.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetFuzzy.restype = c_int
lib.mdMUMatchcodeComponentSetFuzzy.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetFuzzy.restype = None
lib.mdMUMatchcodeComponentGetNear.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetNear.restype = c_int
lib.mdMUMatchcodeComponentSetNear.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetNear.restype = None
lib.mdMUMatchcodeComponentGetNearDbl.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetNearDbl.restype = c_double
lib.mdMUMatchcodeComponentSetNearDbl.argtypes = [c_void_p, c_double]
lib.mdMUMatchcodeComponentSetNearDbl.restype = None
lib.mdMUMatchcodeComponentGetFieldMatch.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetFieldMatch.restype = c_int
lib.mdMUMatchcodeComponentSetFieldMatch.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetFieldMatch.restype = None
lib.mdMUMatchcodeComponentGetSwap.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetSwap.restype = c_int
lib.mdMUMatchcodeComponentSetSwap.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetSwap.restype = None
lib.mdMUMatchcodeComponentGetCombination.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetCombination.restype = c_int
lib.mdMUMatchcodeComponentSetCombination.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentSetCombination.restype = None
lib.mdMUMatchcodeComponentGetComponentCountryTypeFromEnum.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentGetComponentCountryTypeFromEnum.restype = c_int
lib.mdMUMatchcodeComponentGetComponentDescription.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentGetComponentDescription.restype = c_char_p
lib.mdMUMatchcodeComponentGetComponentDescriptionFromEnum.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentGetComponentDescriptionFromEnum.restype = c_char_p
lib.mdMUMatchcodeComponentGetComponentAbbreviation.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetComponentAbbreviation.restype = c_char_p
lib.mdMUMatchcodeComponentParseComponentDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseComponentDescription.restype = c_int
lib.mdMUMatchcodeComponentGetSizeDescription.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetSizeDescription.restype = c_char_p
lib.mdMUMatchcodeComponentParseSizeDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseSizeDescription.restype = c_int
lib.mdMUMatchcodeComponentParseWordCountDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseWordCountDescription.restype = c_int
lib.mdMUMatchcodeComponentGetStartDescription.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetStartDescription.restype = c_char_p
lib.mdMUMatchcodeComponentParseStartDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseStartDescription.restype = c_int
lib.mdMUMatchcodeComponentParseStartPosDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseStartPosDescription.restype = c_int
lib.mdMUMatchcodeComponentGetFuzzyDescription.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentGetFuzzyDescription.restype = c_char_p
lib.mdMUMatchcodeComponentGetFuzzyDescriptionFromEnum.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentGetFuzzyDescriptionFromEnum.restype = c_char_p
lib.mdMUMatchcodeComponentParseFuzzyDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseFuzzyDescription.restype = c_int
lib.mdMUMatchcodeComponentParseNearDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseNearDescription.restype = c_double
lib.mdMUMatchcodeComponentGetFieldMatchDescription.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetFieldMatchDescription.restype = c_char_p
lib.mdMUMatchcodeComponentParseFieldMatchDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentParseFieldMatchDescription.restype = c_int
lib.mdMUMatchcodeComponentGetSwapDescription.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetSwapDescription.restype = c_char_p
lib.mdMUMatchcodeComponentCanChangeComponentType.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentCanChangeComponentType.restype = c_int
lib.mdMUMatchcodeComponentCanChangeLabel.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentCanChangeLabel.restype = c_int
lib.mdMUMatchcodeComponentCanChangeSize.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentCanChangeSize.restype = c_int
lib.mdMUMatchcodeComponentCanChangeWordCount.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentCanChangeWordCount.restype = c_int
lib.mdMUMatchcodeComponentCanChangeStart.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentCanChangeStart.restype = c_int
lib.mdMUMatchcodeComponentCanChangeTrim.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentCanChangeTrim.restype = c_int
lib.mdMUMatchcodeComponentCanChangeFuzzy.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentCanChangeFuzzy.restype = c_int
lib.mdMUMatchcodeComponentGetSizeMinimum.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetSizeMinimum.restype = c_int
lib.mdMUMatchcodeComponentGetSizeMaximum.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetSizeMaximum.restype = c_int
lib.mdMUMatchcodeComponentGetAllowedStarts.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetAllowedStarts.restype = c_int
lib.mdMUMatchcodeComponentGetAllowedFuzzies.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetAllowedFuzzies.restype = c_int
lib.mdMUMatchcodeComponentIsAllowedFuzzy.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeComponentIsAllowedFuzzy.restype = c_int
lib.mdMUMatchcodeComponentGetFuzzyNearType.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetFuzzyNearType.restype = c_int
lib.mdMUMatchcodeComponentGetNearMinimum.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetNearMinimum.restype = c_double
lib.mdMUMatchcodeComponentGetNearMaximum.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetNearMaximum.restype = c_double
lib.mdMUMatchcodeComponentGetAllowedFieldMatches.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetAllowedFieldMatches.restype = c_int
lib.mdMUMatchcodeComponentGetAllowedCombinations.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetAllowedCombinations.restype = c_int
lib.mdMUMatchcodeComponentGetAllowedSwaps.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetAllowedSwaps.restype = c_int
lib.mdMUMatchcodeComponentGetComponentTypeEnum.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetComponentTypeEnum.restype = c_char_p
lib.mdMUMatchcodeComponentGetFuzzyEnum.argtypes = [c_void_p]
lib.mdMUMatchcodeComponentGetFuzzyEnum.restype = c_char_p
lib.mdMUMatchcodeComponentSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdMUMatchcodeComponentSetReserved.restype = None
lib.mdMUMatchcodeComponentGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeComponentGetReserved.restype = c_char_p

lib.mdMUMatchcodeListCreate.argtypes = []
lib.mdMUMatchcodeListCreate.restype = c_void_p
lib.mdMUMatchcodeListDestroy.argtypes = [c_void_p]
lib.mdMUMatchcodeListDestroy.restype = None
lib.mdMUMatchcodeListSetPathToMatchUpFiles.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeListSetPathToMatchUpFiles.restype = None
lib.mdMUMatchcodeListInitializeDataFiles.argtypes = [c_void_p]
lib.mdMUMatchcodeListInitializeDataFiles.restype = c_int
lib.mdMUMatchcodeListGetInitializeErrorString.argtypes = [c_void_p]
lib.mdMUMatchcodeListGetInitializeErrorString.restype = c_char_p
lib.mdMUMatchcodeListGetMatchcodeCount.argtypes = [c_void_p]
lib.mdMUMatchcodeListGetMatchcodeCount.restype = c_int
lib.mdMUMatchcodeListGetMatchcodeName.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeListGetMatchcodeName.restype = c_char_p

lib.mdMUMatchcodeCreate.argtypes = []
lib.mdMUMatchcodeCreate.restype = c_void_p
lib.mdMUMatchcodeDestroy.argtypes = [c_void_p]
lib.mdMUMatchcodeDestroy.restype = None
lib.mdMUMatchcodeSetPathToMatchUpFiles.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeSetPathToMatchUpFiles.restype = None
lib.mdMUMatchcodeInitializeDataFiles.argtypes = [c_void_p]
lib.mdMUMatchcodeInitializeDataFiles.restype = c_int
lib.mdMUMatchcodeGetInitializeErrorString.argtypes = [c_void_p]
lib.mdMUMatchcodeGetInitializeErrorString.restype = c_char_p
lib.mdMUMatchcodeFindMatchcode.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeFindMatchcode.restype = c_int
lib.mdMUMatchcodeGetMatchcodeName.argtypes = [c_void_p]
lib.mdMUMatchcodeGetMatchcodeName.restype = c_char_p
lib.mdMUMatchcodeSetDescription.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeSetDescription.restype = None
lib.mdMUMatchcodeGetDescription.argtypes = [c_void_p]
lib.mdMUMatchcodeGetDescription.restype = c_char_p
lib.mdMUMatchcodeSetNGram.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeSetNGram.restype = None
lib.mdMUMatchcodeGetNGram.argtypes = [c_void_p]
lib.mdMUMatchcodeGetNGram.restype = c_int
lib.mdMUMatchcodeGetMatchcodeItemCount.argtypes = [c_void_p]
lib.mdMUMatchcodeGetMatchcodeItemCount.restype = c_int
lib.mdMUMatchcodeGetMatchcodeItem.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeGetMatchcodeItem.restype = c_void_p
lib.mdMUMatchcodeGetMappingItemCount.argtypes = [c_void_p]
lib.mdMUMatchcodeGetMappingItemCount.restype = c_int
lib.mdMUMatchcodeGetMappingItemType.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeGetMappingItemType.restype = c_int
lib.mdMUMatchcodeGetMappingItemLabel.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeGetMappingItemLabel.restype = c_char_p
lib.mdMUMatchcodeDeleteMatchcodeItem.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeDeleteMatchcodeItem.restype = c_int
lib.mdMUMatchcodeRenameMatchcode.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeRenameMatchcode.restype = c_int
lib.mdMUMatchcodeDeleteMatchcode.argtypes = [c_void_p]
lib.mdMUMatchcodeDeleteMatchcode.restype = c_int
lib.mdMUMatchcodeSave.argtypes = [c_void_p]
lib.mdMUMatchcodeSave.restype = None
lib.mdMUMatchcodeSaveToFile.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeSaveToFile.restype = None
lib.mdMUMatchcodeCreateNewMatchcode.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeCreateNewMatchcode.restype = c_int
lib.mdMUMatchcodeGetRuleDescription.argtypes = [c_void_p, c_int, c_int]
lib.mdMUMatchcodeGetRuleDescription.restype = c_char_p
lib.mdMUMatchcodeGetMaximumCombinations.argtypes = [c_void_p]
lib.mdMUMatchcodeGetMaximumCombinations.restype = c_int
lib.mdMUMatchcodeGetAllowedInputMappingCount.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeGetAllowedInputMappingCount.restype = c_int
lib.mdMUMatchcodeGetAllowedInputMappingType.argtypes = [c_void_p, c_int, c_int]
lib.mdMUMatchcodeGetAllowedInputMappingType.restype = c_int
lib.mdMUMatchcodeGetAllowedInputMappingLabel.argtypes = [c_void_p, c_int, c_int]
lib.mdMUMatchcodeGetAllowedInputMappingLabel.restype = c_char_p
lib.mdMUMatchcodeGetInputMappingLabel.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeGetInputMappingLabel.restype = c_char_p
lib.mdMUMatchcodeParseInputMappingLabel.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeParseInputMappingLabel.restype = c_int
lib.mdMUMatchcodeGetBestInputMappingType.argtypes = [c_void_p, c_int]
lib.mdMUMatchcodeGetBestInputMappingType.restype = c_int
lib.mdMUMatchcodeIsDirectConversion.argtypes = [c_void_p, c_int, c_int]
lib.mdMUMatchcodeIsDirectConversion.restype = c_int
lib.mdMUMatchcodeIsConvertable.argtypes = [c_void_p, c_int, c_int]
lib.mdMUMatchcodeIsConvertable.restype = c_int
lib.mdMUMatchcodeGetInputMappingEnum.argtypes = [c_void_p]
lib.mdMUMatchcodeGetInputMappingEnum.restype = c_char_p
lib.mdMUMatchcodeSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdMUMatchcodeSetReserved.restype = None
lib.mdMUMatchcodeGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdMUMatchcodeGetReserved.restype = c_char_p

lib.mdMUReadWriteCreate.argtypes = []
lib.mdMUReadWriteCreate.restype = c_void_p
lib.mdMUReadWriteDestroy.argtypes = [c_void_p]
lib.mdMUReadWriteDestroy.restype = None
lib.mdMUReadWriteSetPathToMatchUpFiles.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteSetPathToMatchUpFiles.restype = None
lib.mdMUReadWriteSetMatchcodeName.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteSetMatchcodeName.restype = None
lib.mdMUReadWriteSetKeyFile.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteSetKeyFile.restype = None
lib.mdMUReadWriteInitializeDataFiles.argtypes = [c_void_p]
lib.mdMUReadWriteInitializeDataFiles.restype = c_int
lib.mdMUReadWriteGetInitializeErrorString.argtypes = [c_void_p]
lib.mdMUReadWriteGetInitializeErrorString.restype = c_char_p
lib.mdMUReadWriteSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteSetLicenseString.restype = c_int
lib.mdMUReadWriteSetMaximumCharacterSize.argtypes = [c_void_p, c_int]
lib.mdMUReadWriteSetMaximumCharacterSize.restype = None
lib.mdMUReadWriteSetEncoding.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteSetEncoding.restype = c_int
lib.mdMUReadWriteGetBuildNumber.argtypes = [c_void_p]
lib.mdMUReadWriteGetBuildNumber.restype = c_char_p
lib.mdMUReadWriteGetDatabaseDate.argtypes = [c_void_p]
lib.mdMUReadWriteGetDatabaseDate.restype = c_char_p
lib.mdMUReadWriteGetDatabaseExpirationDate.argtypes = [c_void_p]
lib.mdMUReadWriteGetDatabaseExpirationDate.restype = c_char_p
lib.mdMUReadWriteGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdMUReadWriteGetLicenseExpirationDate.restype = c_char_p
lib.mdMUReadWriteGetMatchcodeObject.argtypes = [c_void_p]
lib.mdMUReadWriteGetMatchcodeObject.restype = c_void_p
lib.mdMUReadWriteClearMappings.argtypes = [c_void_p]
lib.mdMUReadWriteClearMappings.restype = None
lib.mdMUReadWriteAddMapping.argtypes = [c_void_p, c_int]
lib.mdMUReadWriteAddMapping.restype = c_int
lib.mdMUReadWriteClearFields.argtypes = [c_void_p]
lib.mdMUReadWriteClearFields.restype = None
lib.mdMUReadWriteAddField.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteAddField.restype = None
lib.mdMUReadWriteBuildKey.argtypes = [c_void_p]
lib.mdMUReadWriteBuildKey.restype = None
lib.mdMUReadWriteSetKey.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteSetKey.restype = None
lib.mdMUReadWriteSetUserInfo.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteSetUserInfo.restype = None
lib.mdMUReadWriteWriteRecord.argtypes = [c_void_p]
lib.mdMUReadWriteWriteRecord.restype = None
lib.mdMUReadWriteProcess.argtypes = [c_void_p]
lib.mdMUReadWriteProcess.restype = None
lib.mdMUReadWriteReadRecord.argtypes = [c_void_p]
lib.mdMUReadWriteReadRecord.restype = c_int
lib.mdMUReadWriteGetKey.argtypes = [c_void_p]
lib.mdMUReadWriteGetKey.restype = c_char_p
lib.mdMUReadWriteGetUserInfo.argtypes = [c_void_p]
lib.mdMUReadWriteGetUserInfo.restype = c_char_p
lib.mdMUReadWriteGetDupeGroup.argtypes = [c_void_p]
lib.mdMUReadWriteGetDupeGroup.restype = c_long
lib.mdMUReadWriteGetStatusCode.argtypes = [c_void_p]
lib.mdMUReadWriteGetStatusCode.restype = c_char_p
lib.mdMUReadWriteGetCount.argtypes = [c_void_p]
lib.mdMUReadWriteGetCount.restype = c_int
lib.mdMUReadWriteGetEntry.argtypes = [c_void_p]
lib.mdMUReadWriteGetEntry.restype = c_int
lib.mdMUReadWriteGetError.argtypes = [c_void_p]
lib.mdMUReadWriteGetError.restype = c_int
lib.mdMUReadWriteGetCombinations.argtypes = [c_void_p]
lib.mdMUReadWriteGetCombinations.restype = c_long
lib.mdMUReadWriteGetFuzzyPercentage.argtypes = [c_void_p]
lib.mdMUReadWriteGetFuzzyPercentage.restype = c_double
lib.mdMUReadWriteGetResults.argtypes = [c_void_p]
lib.mdMUReadWriteGetResults.restype = c_char_p
lib.mdMUReadWriteGetKeySize.argtypes = [c_void_p]
lib.mdMUReadWriteGetKeySize.restype = c_int
lib.mdMUReadWriteSetGroupSorting.argtypes = [c_void_p, c_bool]
lib.mdMUReadWriteSetGroupSorting.restype = None
lib.mdMUReadWriteSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdMUReadWriteSetReserved.restype = None
lib.mdMUReadWriteGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdMUReadWriteGetReserved.restype = c_char_p

lib.mdMUIncrementalCreate.argtypes = []
lib.mdMUIncrementalCreate.restype = c_void_p
lib.mdMUIncrementalDestroy.argtypes = [c_void_p]
lib.mdMUIncrementalDestroy.restype = None
lib.mdMUIncrementalSetPathToMatchUpFiles.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalSetPathToMatchUpFiles.restype = None
lib.mdMUIncrementalSetMatchcodeName.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalSetMatchcodeName.restype = None
lib.mdMUIncrementalSetMustExist.argtypes = [c_void_p, c_bool]
lib.mdMUIncrementalSetMustExist.restype = None
lib.mdMUIncrementalSetKeyFile.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalSetKeyFile.restype = None
lib.mdMUIncrementalInitializeDataFiles.argtypes = [c_void_p]
lib.mdMUIncrementalInitializeDataFiles.restype = c_int
lib.mdMUIncrementalGetInitializeErrorString.argtypes = [c_void_p]
lib.mdMUIncrementalGetInitializeErrorString.restype = c_char_p
lib.mdMUIncrementalSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalSetLicenseString.restype = c_int
lib.mdMUIncrementalSetMaximumCharacterSize.argtypes = [c_void_p, c_int]
lib.mdMUIncrementalSetMaximumCharacterSize.restype = None
lib.mdMUIncrementalSetEncoding.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalSetEncoding.restype = c_int
lib.mdMUIncrementalGetBuildNumber.argtypes = [c_void_p]
lib.mdMUIncrementalGetBuildNumber.restype = c_char_p
lib.mdMUIncrementalGetDatabaseDate.argtypes = [c_void_p]
lib.mdMUIncrementalGetDatabaseDate.restype = c_char_p
lib.mdMUIncrementalGetDatabaseExpirationDate.argtypes = [c_void_p]
lib.mdMUIncrementalGetDatabaseExpirationDate.restype = c_char_p
lib.mdMUIncrementalGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdMUIncrementalGetLicenseExpirationDate.restype = c_char_p
lib.mdMUIncrementalGetMatchcodeObject.argtypes = [c_void_p]
lib.mdMUIncrementalGetMatchcodeObject.restype = c_void_p
lib.mdMUIncrementalClearMappings.argtypes = [c_void_p]
lib.mdMUIncrementalClearMappings.restype = None
lib.mdMUIncrementalAddMapping.argtypes = [c_void_p, c_int]
lib.mdMUIncrementalAddMapping.restype = c_int
lib.mdMUIncrementalClearFields.argtypes = [c_void_p]
lib.mdMUIncrementalClearFields.restype = None
lib.mdMUIncrementalAddField.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalAddField.restype = None
lib.mdMUIncrementalBuildKey.argtypes = [c_void_p]
lib.mdMUIncrementalBuildKey.restype = None
lib.mdMUIncrementalSetKey.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalSetKey.restype = None
lib.mdMUIncrementalSetUserInfo.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalSetUserInfo.restype = None
lib.mdMUIncrementalMatchRecord.argtypes = [c_void_p]
lib.mdMUIncrementalMatchRecord.restype = None
lib.mdMUIncrementalAddRecord.argtypes = [c_void_p]
lib.mdMUIncrementalAddRecord.restype = None
lib.mdMUIncrementalNextMatchingRecord.argtypes = [c_void_p]
lib.mdMUIncrementalNextMatchingRecord.restype = c_int
lib.mdMUIncrementalGetKey.argtypes = [c_void_p]
lib.mdMUIncrementalGetKey.restype = c_char_p
lib.mdMUIncrementalGetUserInfo.argtypes = [c_void_p]
lib.mdMUIncrementalGetUserInfo.restype = c_char_p
lib.mdMUIncrementalGetDupeGroup.argtypes = [c_void_p]
lib.mdMUIncrementalGetDupeGroup.restype = c_long
lib.mdMUIncrementalGetStatusCode.argtypes = [c_void_p]
lib.mdMUIncrementalGetStatusCode.restype = c_char_p
lib.mdMUIncrementalGetCount.argtypes = [c_void_p]
lib.mdMUIncrementalGetCount.restype = c_int
lib.mdMUIncrementalGetEntry.argtypes = [c_void_p]
lib.mdMUIncrementalGetEntry.restype = c_int
lib.mdMUIncrementalGetCombinations.argtypes = [c_void_p]
lib.mdMUIncrementalGetCombinations.restype = c_long
lib.mdMUIncrementalGetResults.argtypes = [c_void_p]
lib.mdMUIncrementalGetResults.restype = c_char_p
lib.mdMUIncrementalGetFuzzyPercentage.argtypes = [c_void_p]
lib.mdMUIncrementalGetFuzzyPercentage.restype = c_double
lib.mdMUIncrementalSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdMUIncrementalSetReserved.restype = None
lib.mdMUIncrementalGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdMUIncrementalGetReserved.restype = c_char_p
lib.mdMUIncrementalBeginTransaction.argtypes = [c_void_p]
lib.mdMUIncrementalBeginTransaction.restype = c_bool
lib.mdMUIncrementalCommitTransaction.argtypes = [c_void_p]
lib.mdMUIncrementalCommitTransaction.restype = c_bool
lib.mdMUIncrementalRollbackTransaction.argtypes = [c_void_p]
lib.mdMUIncrementalRollbackTransaction.restype = c_bool

lib.mdMUHybridCreate.argtypes = []
lib.mdMUHybridCreate.restype = c_void_p
lib.mdMUHybridDestroy.argtypes = [c_void_p]
lib.mdMUHybridDestroy.restype = None
lib.mdMUHybridSetPathToMatchUpFiles.argtypes = [c_void_p, c_char_p]
lib.mdMUHybridSetPathToMatchUpFiles.restype = None
lib.mdMUHybridSetMatchcodeName.argtypes = [c_void_p, c_char_p]
lib.mdMUHybridSetMatchcodeName.restype = None
lib.mdMUHybridInitializeDataFiles.argtypes = [c_void_p]
lib.mdMUHybridInitializeDataFiles.restype = c_int
lib.mdMUHybridGetInitializeErrorString.argtypes = [c_void_p]
lib.mdMUHybridGetInitializeErrorString.restype = c_char_p
lib.mdMUHybridSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdMUHybridSetLicenseString.restype = c_int
lib.mdMUHybridSetMaximumCharacterSize.argtypes = [c_void_p, c_int]
lib.mdMUHybridSetMaximumCharacterSize.restype = None
lib.mdMUHybridSetEncoding.argtypes = [c_void_p, c_char_p]
lib.mdMUHybridSetEncoding.restype = c_int
lib.mdMUHybridGetBuildNumber.argtypes = [c_void_p]
lib.mdMUHybridGetBuildNumber.restype = c_char_p
lib.mdMUHybridGetDatabaseDate.argtypes = [c_void_p]
lib.mdMUHybridGetDatabaseDate.restype = c_char_p
lib.mdMUHybridGetDatabaseExpirationDate.argtypes = [c_void_p]
lib.mdMUHybridGetDatabaseExpirationDate.restype = c_char_p
lib.mdMUHybridGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdMUHybridGetLicenseExpirationDate.restype = c_char_p
lib.mdMUHybridGetMatchcodeObject.argtypes = [c_void_p]
lib.mdMUHybridGetMatchcodeObject.restype = c_void_p
lib.mdMUHybridClearMappings.argtypes = [c_void_p]
lib.mdMUHybridClearMappings.restype = None
lib.mdMUHybridAddMapping.argtypes = [c_void_p, c_int]
lib.mdMUHybridAddMapping.restype = c_int
lib.mdMUHybridClearFields.argtypes = [c_void_p]
lib.mdMUHybridClearFields.restype = None
lib.mdMUHybridAddField.argtypes = [c_void_p, c_char_p]
lib.mdMUHybridAddField.restype = None
lib.mdMUHybridBuildKey.argtypes = [c_void_p]
lib.mdMUHybridBuildKey.restype = None
lib.mdMUHybridGetKey.argtypes = [c_void_p]
lib.mdMUHybridGetKey.restype = c_char_p
lib.mdMUHybridGetKeySize.argtypes = [c_void_p]
lib.mdMUHybridGetKeySize.restype = c_int
lib.mdMUHybridGetClusterSize.argtypes = [c_void_p]
lib.mdMUHybridGetClusterSize.restype = c_int
lib.mdMUHybridCompareKeys.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdMUHybridCompareKeys.restype = c_ulong
lib.mdMUHybridGetResults.argtypes = [c_void_p]
lib.mdMUHybridGetResults.restype = c_char_p
lib.mdMUHybridGetFuzzyPercentage.argtypes = [c_void_p]
lib.mdMUHybridGetFuzzyPercentage.restype = c_double
lib.mdMUHybridSetReserved.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdMUHybridSetReserved.restype = None
lib.mdMUHybridGetReserved.argtypes = [c_void_p, c_char_p]
lib.mdMUHybridGetReserved.restype = c_char_p

# mdMUMatchcodeComponent Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorConfigFile = 1
	ErrorLicenseExpired = 2
	ErrorDatabaseExpired = 3
	ErrorMatchcodeNotSpecified = 4
	ErrorMatchcodeNotFound = 5
	ErrorInvalidMatchcode = 6
	ErrorKeyFile = 7
	ErrorNoneIntersectingGroupCache = 8
	ErrorMatchcodeObsolete = 9
	ErrorGlobalAddrInit = 10
	ErrorIntlLicenseRequired = 11

class MatchcodeComponentType(Enum):
	PrefixComp = 1
	FirstComp = 2
	MiddleComp = 3
	LastComp = 4
	SuffixComp = 5
	GenderComp = 6
	FirstNicknameComp = 7
	MiddleNicknameComp = 8
	TitleComp = 9
	CompanyComp = 10
	CompanyAcronymComp = 11
	StreetNumberComp = 12
	StreetPreDirComp = 13
	StreetNameComp = 14
	StreetSuffixComp = 15
	StreetPostDirComp = 16
	POBoxComp = 17
	SecondaryComp = 18
	AddressComp = 19
	CityComp = 20
	StateComp = 21
	Zip9Comp = 22
	Zip5Comp = 23
	Zip4Comp = 24
	CountryComp = 28
	CanadianPCComp = 29
	PhoneComp = 33
	EMailComp = 34
	CreditCardComp = 35
	GeneralComp = 36
	GeoDistanceComp = 38
	DateComp = 39
	NumericComp = 40
	PremisesNumberComp = 41
	ThoroughfarePreDirComp = 42
	ThoroughfareLeadingTypeComp = 43
	ThoroughfareNameComp = 44
	ThoroughfarePostDirComp = 45
	ThoroughfareTrailingTypeComp = 46
	DepThoroughfarePreDirComp = 47
	DepThoroughfareLeadingTypeComp = 48
	DepThoroughfareNameComp = 49
	DepThoroughfarePostDirComp = 50
	DepThoroughfareTrailingTypeComp = 51
	LocalityComp = 52
	DependentLocalityComp = 53
	DblDependentLocalityComp = 54
	AdministrativeAreaComp = 55
	SubAdministrativeAreaComp = 56
	PostalCodeComp = 57
	SubNationalAreaComp = 58
	PostBoxComp = 59

class MatchcodeStart(Enum):
	Left = 8
	Right = 16
	StartAtPos = 32
	StartAtWord = 64

class MatchcodeTrim(Enum):
	LeftTrim = 2
	RightTrim = 4
	AllTrim = 6

class MatchcodeFuzzy(Enum):
	Exact = 0
	SoundEx = 1
	Phonetex = 2
	Containment = 4
	Frequency = 8
	FastNear = 16
	AccurateNear = 32
	VowelsOnly = 64
	ConsonantsOnly = 128
	AlphasOnly = 256
	NumericsOnly = 512
	FrequencyNear = 1024
	NGram = 2048
	Jaro = 4096
	JaroWinkler = 8192
	LCS = 16384
	NeedlemanWunsch = 32768
	MDKeyboard = 65536
	SmithWatermanGotoh = 131072
	Dice = 262144
	Jaccard = 524288
	Overlap = 1048576
	DoubleMetaphone = 2097152
	UTF8Near = 4194304

class MatchcodeFieldMatch(Enum):
	NoFieldMatch = 0
	BothBlankMatch = 256
	OneBlankMatch = 512
	InitialMatch = 1024

class MatchcodeSwap(Enum):
	NoSwap = 0
	SwapA = 1
	SwapB = 2
	SwapC = 4
	SwapD = 8
	SwapE = 16
	SwapF = 32
	SwapG = 64
	SwapH = 128
	BothA = 256
	BothB = 512
	BothC = 1024
	BothD = 2048
	BothE = 4096
	BothF = 8192
	BothG = 16384
	BothH = 32768

class MatchcodeCombination(Enum):
	Combo1 = 1
	Combo2 = 2
	Combo3 = 4
	Combo4 = 8
	Combo5 = 16
	Combo6 = 32
	Combo7 = 64
	Combo8 = 128
	Combo9 = 256
	Combo10 = 512
	Combo11 = 1024
	Combo12 = 2048
	Combo13 = 4096
	Combo14 = 8192
	Combo15 = 16384
	Combo16 = 32768

class MatchcodeMappingTarget(Enum):
	PrefixType = 1
	FirstType = 2
	MiddleType = 3
	LastType = 4
	SuffixType = 5
	GenderType = 6
	FirstNicknameType = 7
	MiddleNicknameType = 8
	TitleType = 9
	CompanyType = 10
	CompanyAcronymType = 11
	AddressType = 12
	CityType = 13
	StateType = 14
	Zip9Type = 15
	Zip5Type = 16
	Zip4Type = 17
	CountryType = 18
	CanadianPCType = 19
	PhoneType = 23
	EMailType = 24
	CreditCardType = 25
	GeneralType = 26
	Address1Type = 28
	Address2Type = 29
	Address3Type = 30
	LatitudeType = 34
	LongitudeType = 35
	DateType = 36
	NumericType = 37
	Address4Type = 38
	Address5Type = 39
	Address6Type = 40
	Address7Type = 41
	Address8Type = 42

class MatchcodeStatus(Enum):
	MCNoError = 0
	MCFirstComponentFuzzyOptions = 1
	MCFirstComponentNoSwapPair = 2
	MCDataTypeNoFuzzy = 3
	MCComponentFuzzyIncorrectSize = 4
	MCDataTypeNoMaximumNumberWords = 5
	MCDataTypeNoStartRightOrWordOrPos = 6
	MCIncorrectMaximumNumberWords = 7
	MCNearOutOfRange = 8
	MCFirstComponentNotUsedInEveryCondition = 9
	MCCannotChangeFirstComponent = 10
	MCInvalidSwapPair = 11
	MCIncorrectStartPosOrStartWord = 12
	MCInvalidMatchcodeComponentType = 13

class MatchcodeMapping(Enum):
	Prefix = 1
	Gender = 2
	First = 3
	MixedFirst = 4
	Middle = 5
	Last = 6
	MixedLast = 7
	Suffix = 8
	FullName = 9
	InverseName = 10
	GovernmentInverseName = 11
	Title = 12
	Company = 13
	Address = 14
	City = 15
	State = 16
	Zip9 = 17
	Zip5 = 18
	Zip4 = 19
	CityStZip = 20
	Country = 21
	CanadianPostalCode = 22
	Phone = 27
	EMail = 28
	CreditCard = 29
	General = 30
	Latitude = 40
	Longitude = 41
	Date = 42
	Numeric = 43

class MatchcodeNearType(Enum):
	NearNone = 0
	NearInteger = 1
	NearFloat = 2

class ComponentCountryType(Enum):
	US = 1
	Canada = 2
	Global = 4
	Domestic = 3

class mdMUMatchcodeComponent(object):


	def __init__(self):
		self.I = lib.mdMUMatchcodeComponentCreate()

	def __del__(self):
		lib.mdMUMatchcodeComponentDestroy(self.I)

	def GetComponentType(self):
		return MatchcodeComponentType(lib.mdMUMatchcodeComponentGetComponentType(self.I))

	def SetComponentType(self, Type):
		lib.mdMUMatchcodeComponentSetComponentType(self.I, MatchcodeComponentType(Type).value)

	def GetSize(self):
		return lib.mdMUMatchcodeComponentGetSize(self.I)

	def SetSize(self, Size):
		lib.mdMUMatchcodeComponentSetSize(self.I, Size)

	def GetLabel(self):
		return lib.mdMUMatchcodeComponentGetLabel(self.I).decode('utf-8')

	def SetLabel(self, Label):
		lib.mdMUMatchcodeComponentSetLabel(self.I, Label.encode('utf-8'))

	def GetWordCount(self):
		return lib.mdMUMatchcodeComponentGetWordCount(self.I)

	def SetWordCount(self, WordCount):
		lib.mdMUMatchcodeComponentSetWordCount(self.I, WordCount)

	def GetStart(self):
		return MatchcodeStart(lib.mdMUMatchcodeComponentGetStart(self.I))

	def SetStart(self, Start):
		lib.mdMUMatchcodeComponentSetStart(self.I, MatchcodeStart(Start).value)

	def GetStartPos(self):
		return lib.mdMUMatchcodeComponentGetStartPos(self.I)

	def SetStartPos(self, StartPos):
		lib.mdMUMatchcodeComponentSetStartPos(self.I, StartPos)

	def GetTrim(self):
		return MatchcodeTrim(lib.mdMUMatchcodeComponentGetTrim(self.I))

	def SetTrim(self, Trim):
		lib.mdMUMatchcodeComponentSetTrim(self.I, MatchcodeTrim(Trim).value)

	def GetFuzzy(self):
		return MatchcodeFuzzy(lib.mdMUMatchcodeComponentGetFuzzy(self.I))

	def SetFuzzy(self, Fuzzy):
		lib.mdMUMatchcodeComponentSetFuzzy(self.I, MatchcodeFuzzy(Fuzzy).value)

	def GetNear(self):
		return lib.mdMUMatchcodeComponentGetNear(self.I)

	def SetNear(self, Near):
		lib.mdMUMatchcodeComponentSetNear(self.I, Near)

	def GetNearDbl(self):
		return lib.mdMUMatchcodeComponentGetNearDbl(self.I)

	def SetNearDbl(self, Near):
		lib.mdMUMatchcodeComponentSetNearDbl(self.I)

	def GetFieldMatch(self):
		return MatchcodeFieldMatch(lib.mdMUMatchcodeComponentGetFieldMatch(self.I))

	def SetFieldMatch(self, Match):
		lib.mdMUMatchcodeComponentSetFieldMatch(self.I, MatchcodeFieldMatch(Match).value)

	def GetSwap(self):
		return MatchcodeSwap(lib.mdMUMatchcodeComponentGetSwap(self.I))

	def SetSwap(self, Swap):
		lib.mdMUMatchcodeComponentSetSwap(self.I, MatchcodeSwap(Swap).value)

	def GetCombination(self):
		return MatchcodeCombination(lib.mdMUMatchcodeComponentGetCombination(self.I))

	def SetCombination(self, Combination):
		lib.mdMUMatchcodeComponentSetCombination(self.I, MatchcodeCombination(Combination).value)

	def GetComponentCountryTypeFromEnum(self, Value):
		return ComponentCountryType(lib.mdMUMatchcodeComponentGetComponentCountryTypeFromEnum(self.I, MatchcodeComponentType(Value).value))

	def GetComponentDescription(self, UseLabel):
		return lib.mdMUMatchcodeComponentGetComponentDescription(self.I, UseLabel).decode('utf-8')

	def GetComponentDescriptionFromEnum(self, Value):
		return lib.mdMUMatchcodeComponentGetComponentDescriptionFromEnum(self.I, MatchcodeComponentType(Value).value).decode('utf-8')

	def GetComponentAbbreviation(self):
		return lib.mdMUMatchcodeComponentGetComponentAbbreviation(self.I).decode('utf-8')

	def ParseComponentDescription(self, Value):
		return MatchcodeComponentType(lib.mdMUMatchcodeComponentParseComponentDescription(self.I, Value.encode('utf-8')))

	def GetSizeDescription(self):
		return lib.mdMUMatchcodeComponentGetSizeDescription(self.I).decode('utf-8')

	def ParseSizeDescription(self, Value):
		return lib.mdMUMatchcodeComponentParseSizeDescription(self.I, Value.encode('utf-8'))

	def ParseWordCountDescription(self, Value):
		return lib.mdMUMatchcodeComponentParseWordCountDescription(self.I, Value.encode('utf-8'))

	def GetStartDescription(self):
		return lib.mdMUMatchcodeComponentGetStartDescription(self.I).decode('utf-8')

	def ParseStartDescription(self, Value):
		return MatchcodeStart(lib.mdMUMatchcodeComponentParseStartDescription(self.I, Value.encode('utf-8')))

	def ParseStartPosDescription(self, Value):
		return lib.mdMUMatchcodeComponentParseStartPosDescription(self.I, Value.encode('utf-8'))

	def GetFuzzyDescription(self, Decorated):
		return lib.mdMUMatchcodeComponentGetFuzzyDescription(self.I, Decorated).decode('utf-8')

	def GetFuzzyDescriptionFromEnum(self, Value):
		return lib.mdMUMatchcodeComponentGetFuzzyDescriptionFromEnum(self.I, MatchcodeFuzzy(Value).value).decode('utf-8')

	def ParseFuzzyDescription(self, Value):
		return MatchcodeFuzzy(lib.mdMUMatchcodeComponentParseFuzzyDescription(self.I, Value.encode('utf-8')))

	def ParseNearDescription(self, Value):
		return lib.mdMUMatchcodeComponentParseNearDescription(self.I, Value.encode('utf-8'))

	def GetFieldMatchDescription(self):
		return lib.mdMUMatchcodeComponentGetFieldMatchDescription(self.I).decode('utf-8')

	def ParseFieldMatchDescription(self, Value):
		return MatchcodeFieldMatch(lib.mdMUMatchcodeComponentParseFieldMatchDescription(self.I, Value.encode('utf-8')))

	def GetSwapDescription(self):
		return lib.mdMUMatchcodeComponentGetSwapDescription(self.I).decode('utf-8')

	def CanChangeComponentType(self):
		return lib.mdMUMatchcodeComponentCanChangeComponentType(self.I)

	def CanChangeLabel(self):
		return lib.mdMUMatchcodeComponentCanChangeLabel(self.I)

	def CanChangeSize(self):
		return lib.mdMUMatchcodeComponentCanChangeSize(self.I)

	def CanChangeWordCount(self):
		return lib.mdMUMatchcodeComponentCanChangeWordCount(self.I)

	def CanChangeStart(self):
		return lib.mdMUMatchcodeComponentCanChangeStart(self.I)

	def CanChangeTrim(self):
		return lib.mdMUMatchcodeComponentCanChangeTrim(self.I)

	def CanChangeFuzzy(self):
		return lib.mdMUMatchcodeComponentCanChangeFuzzy(self.I)

	def GetSizeMinimum(self):
		return lib.mdMUMatchcodeComponentGetSizeMinimum(self.I)

	def GetSizeMaximum(self):
		return lib.mdMUMatchcodeComponentGetSizeMaximum(self.I)

	def GetAllowedStarts(self):
		return MatchcodeStart(lib.mdMUMatchcodeComponentGetAllowedStarts(self.I))

	def GetAllowedFuzzies(self):
		return MatchcodeFuzzy(lib.mdMUMatchcodeComponentGetAllowedFuzzies(self.I))

	def IsAllowedFuzzy(self, Value):
		return lib.mdMUMatchcodeComponentIsAllowedFuzzy(self.I, MatchcodeFuzzy(Value).value)

	def GetFuzzyNearType(self):
		return MatchcodeNearType(lib.mdMUMatchcodeComponentGetFuzzyNearType(self.I))

	def GetNearMinimum(self):
		return lib.mdMUMatchcodeComponentGetNearMinimum(self.I)

	def GetNearMaximum(self):
		return lib.mdMUMatchcodeComponentGetNearMaximum(self.I)

	def GetAllowedFieldMatches(self):
		return MatchcodeFieldMatch(lib.mdMUMatchcodeComponentGetAllowedFieldMatches(self.I))

	def GetAllowedCombinations(self):
		return MatchcodeCombination(lib.mdMUMatchcodeComponentGetAllowedCombinations(self.I))

	def GetAllowedSwaps(self):
		return MatchcodeSwap(lib.mdMUMatchcodeComponentGetAllowedSwaps(self.I))

	def GetComponentTypeEnum(self):
		return lib.mdMUMatchcodeComponentGetComponentTypeEnum(self.I).decode('utf-8')

	def GetFuzzyEnum(self):
		return lib.mdMUMatchcodeComponentGetFuzzyEnum(self.I).decode('utf-8')

	def SetReserved(self, Property, Value):
		lib.mdMUMatchcodeComponentSetReserved(self.I, Property.encode('utf-8'), Value.encode('utf-8'))

	def GetReserved(self, Property):
		return lib.mdMUMatchcodeComponentGetReserved(self.I, Property.encode('utf-8')).decode('utf-8')

# mdMUMatchcodeList Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorConfigFile = 1
	ErrorLicenseExpired = 2
	ErrorDatabaseExpired = 3
	ErrorMatchcodeNotSpecified = 4
	ErrorMatchcodeNotFound = 5
	ErrorInvalidMatchcode = 6
	ErrorKeyFile = 7
	ErrorNoneIntersectingGroupCache = 8
	ErrorMatchcodeObsolete = 9
	ErrorGlobalAddrInit = 10
	ErrorIntlLicenseRequired = 11

class MatchcodeComponentType(Enum):
	PrefixComp = 1
	FirstComp = 2
	MiddleComp = 3
	LastComp = 4
	SuffixComp = 5
	GenderComp = 6
	FirstNicknameComp = 7
	MiddleNicknameComp = 8
	TitleComp = 9
	CompanyComp = 10
	CompanyAcronymComp = 11
	StreetNumberComp = 12
	StreetPreDirComp = 13
	StreetNameComp = 14
	StreetSuffixComp = 15
	StreetPostDirComp = 16
	POBoxComp = 17
	SecondaryComp = 18
	AddressComp = 19
	CityComp = 20
	StateComp = 21
	Zip9Comp = 22
	Zip5Comp = 23
	Zip4Comp = 24
	CountryComp = 28
	CanadianPCComp = 29
	PhoneComp = 33
	EMailComp = 34
	CreditCardComp = 35
	GeneralComp = 36
	GeoDistanceComp = 38
	DateComp = 39
	NumericComp = 40
	PremisesNumberComp = 41
	ThoroughfarePreDirComp = 42
	ThoroughfareLeadingTypeComp = 43
	ThoroughfareNameComp = 44
	ThoroughfarePostDirComp = 45
	ThoroughfareTrailingTypeComp = 46
	DepThoroughfarePreDirComp = 47
	DepThoroughfareLeadingTypeComp = 48
	DepThoroughfareNameComp = 49
	DepThoroughfarePostDirComp = 50
	DepThoroughfareTrailingTypeComp = 51
	LocalityComp = 52
	DependentLocalityComp = 53
	DblDependentLocalityComp = 54
	AdministrativeAreaComp = 55
	SubAdministrativeAreaComp = 56
	PostalCodeComp = 57
	SubNationalAreaComp = 58
	PostBoxComp = 59

class MatchcodeStart(Enum):
	Left = 8
	Right = 16
	StartAtPos = 32
	StartAtWord = 64

class MatchcodeTrim(Enum):
	LeftTrim = 2
	RightTrim = 4
	AllTrim = 6

class MatchcodeFuzzy(Enum):
	Exact = 0
	SoundEx = 1
	Phonetex = 2
	Containment = 4
	Frequency = 8
	FastNear = 16
	AccurateNear = 32
	VowelsOnly = 64
	ConsonantsOnly = 128
	AlphasOnly = 256
	NumericsOnly = 512
	FrequencyNear = 1024
	NGram = 2048
	Jaro = 4096
	JaroWinkler = 8192
	LCS = 16384
	NeedlemanWunsch = 32768
	MDKeyboard = 65536
	SmithWatermanGotoh = 131072
	Dice = 262144
	Jaccard = 524288
	Overlap = 1048576
	DoubleMetaphone = 2097152
	UTF8Near = 4194304

class MatchcodeFieldMatch(Enum):
	NoFieldMatch = 0
	BothBlankMatch = 256
	OneBlankMatch = 512
	InitialMatch = 1024

class MatchcodeSwap(Enum):
	NoSwap = 0
	SwapA = 1
	SwapB = 2
	SwapC = 4
	SwapD = 8
	SwapE = 16
	SwapF = 32
	SwapG = 64
	SwapH = 128
	BothA = 256
	BothB = 512
	BothC = 1024
	BothD = 2048
	BothE = 4096
	BothF = 8192
	BothG = 16384
	BothH = 32768

class MatchcodeCombination(Enum):
	Combo1 = 1
	Combo2 = 2
	Combo3 = 4
	Combo4 = 8
	Combo5 = 16
	Combo6 = 32
	Combo7 = 64
	Combo8 = 128
	Combo9 = 256
	Combo10 = 512
	Combo11 = 1024
	Combo12 = 2048
	Combo13 = 4096
	Combo14 = 8192
	Combo15 = 16384
	Combo16 = 32768

class MatchcodeMappingTarget(Enum):
	PrefixType = 1
	FirstType = 2
	MiddleType = 3
	LastType = 4
	SuffixType = 5
	GenderType = 6
	FirstNicknameType = 7
	MiddleNicknameType = 8
	TitleType = 9
	CompanyType = 10
	CompanyAcronymType = 11
	AddressType = 12
	CityType = 13
	StateType = 14
	Zip9Type = 15
	Zip5Type = 16
	Zip4Type = 17
	CountryType = 18
	CanadianPCType = 19
	PhoneType = 23
	EMailType = 24
	CreditCardType = 25
	GeneralType = 26
	Address1Type = 28
	Address2Type = 29
	Address3Type = 30
	LatitudeType = 34
	LongitudeType = 35
	DateType = 36
	NumericType = 37
	Address4Type = 38
	Address5Type = 39
	Address6Type = 40
	Address7Type = 41
	Address8Type = 42

class MatchcodeStatus(Enum):
	MCNoError = 0
	MCFirstComponentFuzzyOptions = 1
	MCFirstComponentNoSwapPair = 2
	MCDataTypeNoFuzzy = 3
	MCComponentFuzzyIncorrectSize = 4
	MCDataTypeNoMaximumNumberWords = 5
	MCDataTypeNoStartRightOrWordOrPos = 6
	MCIncorrectMaximumNumberWords = 7
	MCNearOutOfRange = 8
	MCFirstComponentNotUsedInEveryCondition = 9
	MCCannotChangeFirstComponent = 10
	MCInvalidSwapPair = 11
	MCIncorrectStartPosOrStartWord = 12
	MCInvalidMatchcodeComponentType = 13

class MatchcodeMapping(Enum):
	Prefix = 1
	Gender = 2
	First = 3
	MixedFirst = 4
	Middle = 5
	Last = 6
	MixedLast = 7
	Suffix = 8
	FullName = 9
	InverseName = 10
	GovernmentInverseName = 11
	Title = 12
	Company = 13
	Address = 14
	City = 15
	State = 16
	Zip9 = 17
	Zip5 = 18
	Zip4 = 19
	CityStZip = 20
	Country = 21
	CanadianPostalCode = 22
	Phone = 27
	EMail = 28
	CreditCard = 29
	General = 30
	Latitude = 40
	Longitude = 41
	Date = 42
	Numeric = 43

class MatchcodeNearType(Enum):
	NearNone = 0
	NearInteger = 1
	NearFloat = 2

class ComponentCountryType(Enum):
	US = 1
	Canada = 2
	Global = 4
	Domestic = 3

class mdMUMatchcodeList(object):
	def __init__(self):
		self.I = lib.mdMUMatchcodeListCreate()

	def __del__(self):
		lib.mdMUMatchcodeListDestroy(self.I)

	def SetPathToMatchUpFiles(self, Path):
		lib.mdMUMatchcodeListSetPathToMatchUpFiles(self.I, Path.encode('utf-8'))

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdMUMatchcodeListInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdMUMatchcodeListGetInitializeErrorString(self.I).decode('utf-8')

	def GetMatchcodeCount(self):
		return lib.mdMUMatchcodeListGetMatchcodeCount(self.I)

	def GetMatchcodeName(self, Pos):
		return lib.mdMUMatchcodeListGetMatchcodeName(self.I, Pos).decode('utf-8')

# mdMUMatchcode Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorConfigFile = 1
	ErrorLicenseExpired = 2
	ErrorDatabaseExpired = 3
	ErrorMatchcodeNotSpecified = 4
	ErrorMatchcodeNotFound = 5
	ErrorInvalidMatchcode = 6
	ErrorKeyFile = 7
	ErrorNoneIntersectingGroupCache = 8
	ErrorMatchcodeObsolete = 9
	ErrorGlobalAddrInit = 10
	ErrorIntlLicenseRequired = 11

class MatchcodeComponentType(Enum):
	PrefixComp = 1
	FirstComp = 2
	MiddleComp = 3
	LastComp = 4
	SuffixComp = 5
	GenderComp = 6
	FirstNicknameComp = 7
	MiddleNicknameComp = 8
	TitleComp = 9
	CompanyComp = 10
	CompanyAcronymComp = 11
	StreetNumberComp = 12
	StreetPreDirComp = 13
	StreetNameComp = 14
	StreetSuffixComp = 15
	StreetPostDirComp = 16
	POBoxComp = 17
	SecondaryComp = 18
	AddressComp = 19
	CityComp = 20
	StateComp = 21
	Zip9Comp = 22
	Zip5Comp = 23
	Zip4Comp = 24
	CountryComp = 28
	CanadianPCComp = 29
	PhoneComp = 33
	EMailComp = 34
	CreditCardComp = 35
	GeneralComp = 36
	GeoDistanceComp = 38
	DateComp = 39
	NumericComp = 40
	PremisesNumberComp = 41
	ThoroughfarePreDirComp = 42
	ThoroughfareLeadingTypeComp = 43
	ThoroughfareNameComp = 44
	ThoroughfarePostDirComp = 45
	ThoroughfareTrailingTypeComp = 46
	DepThoroughfarePreDirComp = 47
	DepThoroughfareLeadingTypeComp = 48
	DepThoroughfareNameComp = 49
	DepThoroughfarePostDirComp = 50
	DepThoroughfareTrailingTypeComp = 51
	LocalityComp = 52
	DependentLocalityComp = 53
	DblDependentLocalityComp = 54
	AdministrativeAreaComp = 55
	SubAdministrativeAreaComp = 56
	PostalCodeComp = 57
	SubNationalAreaComp = 58
	PostBoxComp = 59

class MatchcodeStart(Enum):
	Left = 8
	Right = 16
	StartAtPos = 32
	StartAtWord = 64

class MatchcodeTrim(Enum):
	LeftTrim = 2
	RightTrim = 4
	AllTrim = 6

class MatchcodeFuzzy(Enum):
	Exact = 0
	SoundEx = 1
	Phonetex = 2
	Containment = 4
	Frequency = 8
	FastNear = 16
	AccurateNear = 32
	VowelsOnly = 64
	ConsonantsOnly = 128
	AlphasOnly = 256
	NumericsOnly = 512
	FrequencyNear = 1024
	NGram = 2048
	Jaro = 4096
	JaroWinkler = 8192
	LCS = 16384
	NeedlemanWunsch = 32768
	MDKeyboard = 65536
	SmithWatermanGotoh = 131072
	Dice = 262144
	Jaccard = 524288
	Overlap = 1048576
	DoubleMetaphone = 2097152
	UTF8Near = 4194304

class MatchcodeFieldMatch(Enum):
	NoFieldMatch = 0
	BothBlankMatch = 256
	OneBlankMatch = 512
	InitialMatch = 1024

class MatchcodeSwap(Enum):
	NoSwap = 0
	SwapA = 1
	SwapB = 2
	SwapC = 4
	SwapD = 8
	SwapE = 16
	SwapF = 32
	SwapG = 64
	SwapH = 128
	BothA = 256
	BothB = 512
	BothC = 1024
	BothD = 2048
	BothE = 4096
	BothF = 8192
	BothG = 16384
	BothH = 32768

class MatchcodeCombination(Enum):
	Combo1 = 1
	Combo2 = 2
	Combo3 = 4
	Combo4 = 8
	Combo5 = 16
	Combo6 = 32
	Combo7 = 64
	Combo8 = 128
	Combo9 = 256
	Combo10 = 512
	Combo11 = 1024
	Combo12 = 2048
	Combo13 = 4096
	Combo14 = 8192
	Combo15 = 16384
	Combo16 = 32768

class MatchcodeMappingTarget(Enum):
	PrefixType = 1
	FirstType = 2
	MiddleType = 3
	LastType = 4
	SuffixType = 5
	GenderType = 6
	FirstNicknameType = 7
	MiddleNicknameType = 8
	TitleType = 9
	CompanyType = 10
	CompanyAcronymType = 11
	AddressType = 12
	CityType = 13
	StateType = 14
	Zip9Type = 15
	Zip5Type = 16
	Zip4Type = 17
	CountryType = 18
	CanadianPCType = 19
	PhoneType = 23
	EMailType = 24
	CreditCardType = 25
	GeneralType = 26
	Address1Type = 28
	Address2Type = 29
	Address3Type = 30
	LatitudeType = 34
	LongitudeType = 35
	DateType = 36
	NumericType = 37
	Address4Type = 38
	Address5Type = 39
	Address6Type = 40
	Address7Type = 41
	Address8Type = 42

class MatchcodeStatus(Enum):
	MCNoError = 0
	MCFirstComponentFuzzyOptions = 1
	MCFirstComponentNoSwapPair = 2
	MCDataTypeNoFuzzy = 3
	MCComponentFuzzyIncorrectSize = 4
	MCDataTypeNoMaximumNumberWords = 5
	MCDataTypeNoStartRightOrWordOrPos = 6
	MCIncorrectMaximumNumberWords = 7
	MCNearOutOfRange = 8
	MCFirstComponentNotUsedInEveryCondition = 9
	MCCannotChangeFirstComponent = 10
	MCInvalidSwapPair = 11
	MCIncorrectStartPosOrStartWord = 12
	MCInvalidMatchcodeComponentType = 13

class MatchcodeMapping(Enum):
	Prefix = 1
	Gender = 2
	First = 3
	MixedFirst = 4
	Middle = 5
	Last = 6
	MixedLast = 7
	Suffix = 8
	FullName = 9
	InverseName = 10
	GovernmentInverseName = 11
	Title = 12
	Company = 13
	Address = 14
	City = 15
	State = 16
	Zip9 = 17
	Zip5 = 18
	Zip4 = 19
	CityStZip = 20
	Country = 21
	CanadianPostalCode = 22
	Phone = 27
	EMail = 28
	CreditCard = 29
	General = 30
	Latitude = 40
	Longitude = 41
	Date = 42
	Numeric = 43

class MatchcodeNearType(Enum):
	NearNone = 0
	NearInteger = 1
	NearFloat = 2

class ComponentCountryType(Enum):
	US = 1
	Canada = 2
	Global = 4
	Domestic = 3

class mdMUMatchcode(object):


	def __init__(self):
		self.I = lib.mdMUMatchcodeCreate()

	def __del__(self):
		lib.mdMUMatchcodeDestroy(self.I)

	def SetPathToMatchUpFiles(self, Path):
		lib.mdMUMatchcodeSetPathToMatchUpFiles(self.I, Path.encode('utf-8'))

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdMUMatchcodeInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdMUMatchcodeGetInitializeErrorString(self.I).decode('utf-8')

	def FindMatchcode(self, Matchcode):
		return lib.mdMUMatchcodeFindMatchcode(self.I, Matchcode.encode('utf-8'))

	def GetMatchcodeName(self):
		return lib.mdMUMatchcodeGetMatchcodeName(self.I).decode('utf-8')

	def SetDescription(self, Description):
		lib.mdMUMatchcodeSetDescription(self.I, Description.encode('utf-8'))

	def GetDescription(self):
		return lib.mdMUMatchcodeGetDescription(self.I).decode('utf-8')

	def SetNGram(self, NGram):
		lib.mdMUMatchcodeSetNGram(self.I, NGram)

	def GetNGram(self):
		return lib.mdMUMatchcodeGetNGram(self.I)

	def GetMatchcodeItemCount(self):
		return lib.mdMUMatchcodeGetMatchcodeItemCount(self.I)

	def GetMatchcodeItem(self, Pos):
		return lib.mdMUMatchcodeGetMatchcodeItem(self.I, Pos)

	def GetMappingItemCount(self):
		return lib.mdMUMatchcodeGetMappingItemCount(self.I)

	def GetMappingItemType(self, Pos):
		return MatchcodeMappingTarget(lib.mdMUMatchcodeGetMappingItemType(self.I, Pos))

	def GetMappingItemLabel(self, Pos):
		return lib.mdMUMatchcodeGetMappingItemLabel(self.I, Pos).decode('utf-8')

	def DeleteMatchcodeItem(self, Pos):
		return MatchcodeStatus(lib.mdMUMatchcodeDeleteMatchcodeItem(self.I, Pos))

	def RenameMatchcode(self, Name):
		return lib.mdMUMatchcodeRenameMatchcode(self.I, Name.encode('utf-8'))

	def DeleteMatchcode(self):
		return lib.mdMUMatchcodeDeleteMatchcode(self.I)

	def Save(self):
		lib.mdMUMatchcodeSave(self.I)

	def SaveToFile(self, Path):
		lib.mdMUMatchcodeSaveToFile(self.I, Path.encode('utf-8'))

	def CreateNewMatchcode(self, Matchcode):
		return lib.mdMUMatchcodeCreateNewMatchcode(self.I, Matchcode.encode('utf-8'))

	def GetRuleDescription(self, Rule_, Abbreviated_):
		return lib.mdMUMatchcodeGetRuleDescription(self.I, Rule_, Abbreviated_).decode('utf-8')

	def GetMaximumCombinations(self):
		return lib.mdMUMatchcodeGetMaximumCombinations(self.I)

	def GetAllowedInputMappingCount(self, Mapping_):
		return lib.mdMUMatchcodeGetAllowedInputMappingCount(self.I, MatchcodeMappingTarget(Mapping_).value)

	def GetAllowedInputMappingType(self, Mapping_, Pos_):
		return MatchcodeMapping(lib.mdMUMatchcodeGetAllowedInputMappingType(self.I, MatchcodeMappingTarget(Mapping_).value, Pos_))

	def GetAllowedInputMappingLabel(self, Mapping_, Pos_):
		return lib.mdMUMatchcodeGetAllowedInputMappingLabel(self.I, MatchcodeMappingTarget(Mapping_).value, Pos_).decode('utf-8')

	def GetInputMappingLabel(self, Mapping_):
		return lib.mdMUMatchcodeGetInputMappingLabel(self.I, MatchcodeMapping(Mapping_).value).decode('utf-8')

	def ParseInputMappingLabel(self, Value_):
		return MatchcodeMapping(lib.mdMUMatchcodeParseInputMappingLabel(self.I, Value_.encode('utf-8')))

	def GetBestInputMappingType(self, Target_):
		return MatchcodeMapping(lib.mdMUMatchcodeGetBestInputMappingType(self.I, MatchcodeMappingTarget(Target_).value))

	def IsDirectConversion(self, Source_, Target_):
		return lib.mdMUMatchcodeIsDirectConversion(self.I, MatchcodeMapping(Source_).value, MatchcodeMappingTarget(Target_).value)

	def IsConvertable(self, Source_, Target_):
		return lib.mdMUMatchcodeIsConvertable(self.I, MatchcodeMapping(Source_).value, MatchcodeMappingTarget(Target_).value)

	def GetInputMappingEnum(self):
		return lib.mdMUMatchcodeGetInputMappingEnum(self.I).decode('utf-8')

	def SetReserved(self, Property, Value):
		lib.mdMUMatchcodeSetReserved(self.I, Property.encode('utf-8'), Value.encode('utf-8'))

	def GetReserved(self, Property):
		return lib.mdMUMatchcodeGetReserved(self.I, Property.encode('utf-8')).decode('utf-8')

# mdMUReadWrite Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorConfigFile = 1
	ErrorLicenseExpired = 2
	ErrorDatabaseExpired = 3
	ErrorMatchcodeNotSpecified = 4
	ErrorMatchcodeNotFound = 5
	ErrorInvalidMatchcode = 6
	ErrorKeyFile = 7
	ErrorNoneIntersectingGroupCache = 8
	ErrorMatchcodeObsolete = 9
	ErrorGlobalAddrInit = 10
	ErrorIntlLicenseRequired = 11

class MatchcodeComponentType(Enum):
	PrefixComp = 1
	FirstComp = 2
	MiddleComp = 3
	LastComp = 4
	SuffixComp = 5
	GenderComp = 6
	FirstNicknameComp = 7
	MiddleNicknameComp = 8
	TitleComp = 9
	CompanyComp = 10
	CompanyAcronymComp = 11
	StreetNumberComp = 12
	StreetPreDirComp = 13
	StreetNameComp = 14
	StreetSuffixComp = 15
	StreetPostDirComp = 16
	POBoxComp = 17
	SecondaryComp = 18
	AddressComp = 19
	CityComp = 20
	StateComp = 21
	Zip9Comp = 22
	Zip5Comp = 23
	Zip4Comp = 24
	CountryComp = 28
	CanadianPCComp = 29
	PhoneComp = 33
	EMailComp = 34
	CreditCardComp = 35
	GeneralComp = 36
	GeoDistanceComp = 38
	DateComp = 39
	NumericComp = 40
	PremisesNumberComp = 41
	ThoroughfarePreDirComp = 42
	ThoroughfareLeadingTypeComp = 43
	ThoroughfareNameComp = 44
	ThoroughfarePostDirComp = 45
	ThoroughfareTrailingTypeComp = 46
	DepThoroughfarePreDirComp = 47
	DepThoroughfareLeadingTypeComp = 48
	DepThoroughfareNameComp = 49
	DepThoroughfarePostDirComp = 50
	DepThoroughfareTrailingTypeComp = 51
	LocalityComp = 52
	DependentLocalityComp = 53
	DblDependentLocalityComp = 54
	AdministrativeAreaComp = 55
	SubAdministrativeAreaComp = 56
	PostalCodeComp = 57
	SubNationalAreaComp = 58
	PostBoxComp = 59

class MatchcodeStart(Enum):
	Left = 8
	Right = 16
	StartAtPos = 32
	StartAtWord = 64

class MatchcodeTrim(Enum):
	LeftTrim = 2
	RightTrim = 4
	AllTrim = 6

class MatchcodeFuzzy(Enum):
	Exact = 0
	SoundEx = 1
	Phonetex = 2
	Containment = 4
	Frequency = 8
	FastNear = 16
	AccurateNear = 32
	VowelsOnly = 64
	ConsonantsOnly = 128
	AlphasOnly = 256
	NumericsOnly = 512
	FrequencyNear = 1024
	NGram = 2048
	Jaro = 4096
	JaroWinkler = 8192
	LCS = 16384
	NeedlemanWunsch = 32768
	MDKeyboard = 65536
	SmithWatermanGotoh = 131072
	Dice = 262144
	Jaccard = 524288
	Overlap = 1048576
	DoubleMetaphone = 2097152
	UTF8Near = 4194304

class MatchcodeFieldMatch(Enum):
	NoFieldMatch = 0
	BothBlankMatch = 256
	OneBlankMatch = 512
	InitialMatch = 1024

class MatchcodeSwap(Enum):
	NoSwap = 0
	SwapA = 1
	SwapB = 2
	SwapC = 4
	SwapD = 8
	SwapE = 16
	SwapF = 32
	SwapG = 64
	SwapH = 128
	BothA = 256
	BothB = 512
	BothC = 1024
	BothD = 2048
	BothE = 4096
	BothF = 8192
	BothG = 16384
	BothH = 32768

class MatchcodeCombination(Enum):
	Combo1 = 1
	Combo2 = 2
	Combo3 = 4
	Combo4 = 8
	Combo5 = 16
	Combo6 = 32
	Combo7 = 64
	Combo8 = 128
	Combo9 = 256
	Combo10 = 512
	Combo11 = 1024
	Combo12 = 2048
	Combo13 = 4096
	Combo14 = 8192
	Combo15 = 16384
	Combo16 = 32768

class MatchcodeMappingTarget(Enum):
	PrefixType = 1
	FirstType = 2
	MiddleType = 3
	LastType = 4
	SuffixType = 5
	GenderType = 6
	FirstNicknameType = 7
	MiddleNicknameType = 8
	TitleType = 9
	CompanyType = 10
	CompanyAcronymType = 11
	AddressType = 12
	CityType = 13
	StateType = 14
	Zip9Type = 15
	Zip5Type = 16
	Zip4Type = 17
	CountryType = 18
	CanadianPCType = 19
	PhoneType = 23
	EMailType = 24
	CreditCardType = 25
	GeneralType = 26
	Address1Type = 28
	Address2Type = 29
	Address3Type = 30
	LatitudeType = 34
	LongitudeType = 35
	DateType = 36
	NumericType = 37
	Address4Type = 38
	Address5Type = 39
	Address6Type = 40
	Address7Type = 41
	Address8Type = 42

class MatchcodeStatus(Enum):
	MCNoError = 0
	MCFirstComponentFuzzyOptions = 1
	MCFirstComponentNoSwapPair = 2
	MCDataTypeNoFuzzy = 3
	MCComponentFuzzyIncorrectSize = 4
	MCDataTypeNoMaximumNumberWords = 5
	MCDataTypeNoStartRightOrWordOrPos = 6
	MCIncorrectMaximumNumberWords = 7
	MCNearOutOfRange = 8
	MCFirstComponentNotUsedInEveryCondition = 9
	MCCannotChangeFirstComponent = 10
	MCInvalidSwapPair = 11
	MCIncorrectStartPosOrStartWord = 12
	MCInvalidMatchcodeComponentType = 13

class MatchcodeMapping(Enum):
	Prefix = 1
	Gender = 2
	First = 3
	MixedFirst = 4
	Middle = 5
	Last = 6
	MixedLast = 7
	Suffix = 8
	FullName = 9
	InverseName = 10
	GovernmentInverseName = 11
	Title = 12
	Company = 13
	Address = 14
	City = 15
	State = 16
	Zip9 = 17
	Zip5 = 18
	Zip4 = 19
	CityStZip = 20
	Country = 21
	CanadianPostalCode = 22
	Phone = 27
	EMail = 28
	CreditCard = 29
	General = 30
	Latitude = 40
	Longitude = 41
	Date = 42
	Numeric = 43

class MatchcodeNearType(Enum):
	NearNone = 0
	NearInteger = 1
	NearFloat = 2

class ComponentCountryType(Enum):
	US = 1
	Canada = 2
	Global = 4
	Domestic = 3

class mdMUReadWrite(object):
	def __init__(self):
		self.I = lib.mdMUReadWriteCreate()

	def __del__(self):
		lib.mdMUReadWriteDestroy(self.I)

	def SetPathToMatchUpFiles(self, Path):
		lib.mdMUReadWriteSetPathToMatchUpFiles(self.I, Path.encode('utf-8'))

	def SetMatchcodeName(self, MatchcodeName):
		lib.mdMUReadWriteSetMatchcodeName(self.I, MatchcodeName.encode('utf-8'))

	def SetKeyFile(self, KeyFile):
		lib.mdMUReadWriteSetKeyFile(self.I, KeyFile.encode('utf-8'))

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdMUReadWriteInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdMUReadWriteGetInitializeErrorString(self.I).decode('utf-8')

	def SetLicenseString(self, License):
		return lib.mdMUReadWriteSetLicenseString(self.I, License.encode('utf-8'))

	def SetMaximumCharacterSize(self, size):
		lib.mdMUReadWriteSetMaximumCharacterSize(self.I, size)

	def SetEncoding(self, encodeName):
		return lib.mdMUReadWriteSetEncoding(self.I, encodeName.encode('utf-8'))

	def GetBuildNumber(self):
		return lib.mdMUReadWriteGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdMUReadWriteGetDatabaseDate(self.I).decode('utf-8')

	def GetDatabaseExpirationDate(self):
		return lib.mdMUReadWriteGetDatabaseExpirationDate(self.I).decode('utf-8')

	def GetLicenseExpirationDate(self):
		return lib.mdMUReadWriteGetLicenseExpirationDate(self.I).decode('utf-8')

	def GetMatchcodeObject(self):
		return lib.mdMUReadWriteGetMatchcodeObject(self.I)

	def ClearMappings(self):
		lib.mdMUReadWriteClearMappings(self.I)

	def AddMapping(self, Mapping):
		return lib.mdMUReadWriteAddMapping(self.I, MatchcodeMapping(Mapping).value)

	def ClearFields(self):
		lib.mdMUReadWriteClearFields(self.I)

	def AddField(self, Field):
		lib.mdMUReadWriteAddField(self.I, Field.encode('utf-8'))

	def BuildKey(self):
		lib.mdMUReadWriteBuildKey(self.I)

	def SetKey(self, Key):
		lib.mdMUReadWriteSetKey(self.I, Key.encode('utf-8'))

	def SetUserInfo(self, UserInfo):
		lib.mdMUReadWriteSetUserInfo(self.I, UserInfo.encode('utf-8'))

	def WriteRecord(self):
		lib.mdMUReadWriteWriteRecord(self.I)

	def Process(self):
		lib.mdMUReadWriteProcess(self.I)

	def ReadRecord(self):
		return lib.mdMUReadWriteReadRecord(self.I)

	def GetKey(self):
		return lib.mdMUReadWriteGetKey(self.I).decode('utf-8')

	def GetUserInfo(self):
		return lib.mdMUReadWriteGetUserInfo(self.I).decode('utf-8')

	def GetDupeGroup(self):
		return lib.mdMUReadWriteGetDupeGroup(self.I)

	def GetStatusCode(self):
		return lib.mdMUReadWriteGetStatusCode(self.I).decode('utf-8')

	def GetCount(self):
		return lib.mdMUReadWriteGetCount(self.I)

	def GetEntry(self):
		return lib.mdMUReadWriteGetEntry(self.I)

	def GetError(self):
		return lib.mdMUReadWriteGetError(self.I)

	def GetCombinations(self):
		return lib.mdMUReadWriteGetCombinations(self.I)

	def GetFuzzyPercentage(self):
		return lib.mdMUReadWriteGetFuzzyPercentage(self.I)

	def GetResults(self):
		return lib.mdMUReadWriteGetResults(self.I).decode('utf-8')

	def GetKeySize(self):
		return lib.mdMUReadWriteGetKeySize(self.I)

	def SetGroupSorting(self, bGroupSorting):
		lib.mdMUReadWriteSetGroupSorting(self.I, bGroupSorting)

	def SetReserved(self, Property, Value):
		lib.mdMUReadWriteSetReserved(self.I, Property.encode('utf-8'), Value.encode('utf-8'))

	def GetReserved(self, Property):
		return lib.mdMUReadWriteGetReserved(self.I, Property.encode('utf-8')).decode('utf-8')

# mdMUIncremental Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorConfigFile = 1
	ErrorLicenseExpired = 2
	ErrorDatabaseExpired = 3
	ErrorMatchcodeNotSpecified = 4
	ErrorMatchcodeNotFound = 5
	ErrorInvalidMatchcode = 6
	ErrorKeyFile = 7
	ErrorNoneIntersectingGroupCache = 8
	ErrorMatchcodeObsolete = 9
	ErrorGlobalAddrInit = 10
	ErrorIntlLicenseRequired = 11

class MatchcodeComponentType(Enum):
	PrefixComp = 1
	FirstComp = 2
	MiddleComp = 3
	LastComp = 4
	SuffixComp = 5
	GenderComp = 6
	FirstNicknameComp = 7
	MiddleNicknameComp = 8
	TitleComp = 9
	CompanyComp = 10
	CompanyAcronymComp = 11
	StreetNumberComp = 12
	StreetPreDirComp = 13
	StreetNameComp = 14
	StreetSuffixComp = 15
	StreetPostDirComp = 16
	POBoxComp = 17
	SecondaryComp = 18
	AddressComp = 19
	CityComp = 20
	StateComp = 21
	Zip9Comp = 22
	Zip5Comp = 23
	Zip4Comp = 24
	CountryComp = 28
	CanadianPCComp = 29
	PhoneComp = 33
	EMailComp = 34
	CreditCardComp = 35
	GeneralComp = 36
	GeoDistanceComp = 38
	DateComp = 39
	NumericComp = 40
	PremisesNumberComp = 41
	ThoroughfarePreDirComp = 42
	ThoroughfareLeadingTypeComp = 43
	ThoroughfareNameComp = 44
	ThoroughfarePostDirComp = 45
	ThoroughfareTrailingTypeComp = 46
	DepThoroughfarePreDirComp = 47
	DepThoroughfareLeadingTypeComp = 48
	DepThoroughfareNameComp = 49
	DepThoroughfarePostDirComp = 50
	DepThoroughfareTrailingTypeComp = 51
	LocalityComp = 52
	DependentLocalityComp = 53
	DblDependentLocalityComp = 54
	AdministrativeAreaComp = 55
	SubAdministrativeAreaComp = 56
	PostalCodeComp = 57
	SubNationalAreaComp = 58
	PostBoxComp = 59

class MatchcodeStart(Enum):
	Left = 8
	Right = 16
	StartAtPos = 32
	StartAtWord = 64

class MatchcodeTrim(Enum):
	LeftTrim = 2
	RightTrim = 4
	AllTrim = 6

class MatchcodeFuzzy(Enum):
	Exact = 0
	SoundEx = 1
	Phonetex = 2
	Containment = 4
	Frequency = 8
	FastNear = 16
	AccurateNear = 32
	VowelsOnly = 64
	ConsonantsOnly = 128
	AlphasOnly = 256
	NumericsOnly = 512
	FrequencyNear = 1024
	NGram = 2048
	Jaro = 4096
	JaroWinkler = 8192
	LCS = 16384
	NeedlemanWunsch = 32768
	MDKeyboard = 65536
	SmithWatermanGotoh = 131072
	Dice = 262144
	Jaccard = 524288
	Overlap = 1048576
	DoubleMetaphone = 2097152
	UTF8Near = 4194304

class MatchcodeFieldMatch(Enum):
	NoFieldMatch = 0
	BothBlankMatch = 256
	OneBlankMatch = 512
	InitialMatch = 1024

class MatchcodeSwap(Enum):
	NoSwap = 0
	SwapA = 1
	SwapB = 2
	SwapC = 4
	SwapD = 8
	SwapE = 16
	SwapF = 32
	SwapG = 64
	SwapH = 128
	BothA = 256
	BothB = 512
	BothC = 1024
	BothD = 2048
	BothE = 4096
	BothF = 8192
	BothG = 16384
	BothH = 32768

class MatchcodeCombination(Enum):
	Combo1 = 1
	Combo2 = 2
	Combo3 = 4
	Combo4 = 8
	Combo5 = 16
	Combo6 = 32
	Combo7 = 64
	Combo8 = 128
	Combo9 = 256
	Combo10 = 512
	Combo11 = 1024
	Combo12 = 2048
	Combo13 = 4096
	Combo14 = 8192
	Combo15 = 16384
	Combo16 = 32768

class MatchcodeMappingTarget(Enum):
	PrefixType = 1
	FirstType = 2
	MiddleType = 3
	LastType = 4
	SuffixType = 5
	GenderType = 6
	FirstNicknameType = 7
	MiddleNicknameType = 8
	TitleType = 9
	CompanyType = 10
	CompanyAcronymType = 11
	AddressType = 12
	CityType = 13
	StateType = 14
	Zip9Type = 15
	Zip5Type = 16
	Zip4Type = 17
	CountryType = 18
	CanadianPCType = 19
	PhoneType = 23
	EMailType = 24
	CreditCardType = 25
	GeneralType = 26
	Address1Type = 28
	Address2Type = 29
	Address3Type = 30
	LatitudeType = 34
	LongitudeType = 35
	DateType = 36
	NumericType = 37
	Address4Type = 38
	Address5Type = 39
	Address6Type = 40
	Address7Type = 41
	Address8Type = 42

class MatchcodeStatus(Enum):
	MCNoError = 0
	MCFirstComponentFuzzyOptions = 1
	MCFirstComponentNoSwapPair = 2
	MCDataTypeNoFuzzy = 3
	MCComponentFuzzyIncorrectSize = 4
	MCDataTypeNoMaximumNumberWords = 5
	MCDataTypeNoStartRightOrWordOrPos = 6
	MCIncorrectMaximumNumberWords = 7
	MCNearOutOfRange = 8
	MCFirstComponentNotUsedInEveryCondition = 9
	MCCannotChangeFirstComponent = 10
	MCInvalidSwapPair = 11
	MCIncorrectStartPosOrStartWord = 12
	MCInvalidMatchcodeComponentType = 13

class MatchcodeMapping(Enum):
	Prefix = 1
	Gender = 2
	First = 3
	MixedFirst = 4
	Middle = 5
	Last = 6
	MixedLast = 7
	Suffix = 8
	FullName = 9
	InverseName = 10
	GovernmentInverseName = 11
	Title = 12
	Company = 13
	Address = 14
	City = 15
	State = 16
	Zip9 = 17
	Zip5 = 18
	Zip4 = 19
	CityStZip = 20
	Country = 21
	CanadianPostalCode = 22
	Phone = 27
	EMail = 28
	CreditCard = 29
	General = 30
	Latitude = 40
	Longitude = 41
	Date = 42
	Numeric = 43

class MatchcodeNearType(Enum):
	NearNone = 0
	NearInteger = 1
	NearFloat = 2

class ComponentCountryType(Enum):
	US = 1
	Canada = 2
	Global = 4
	Domestic = 3

class mdMUIncremental(object):
	def __init__(self):
		self.I = lib.mdMUIncrementalCreate()

	def __del__(self):
		lib.mdMUIncrementalDestroy(self.I)

	def SetPathToMatchUpFiles(self, Path):
		lib.mdMUIncrementalSetPathToMatchUpFiles(self.I, Path.encode('utf-8'))

	def SetMatchcodeName(self, MatchcodeName):
		lib.mdMUIncrementalSetMatchcodeName(self.I, MatchcodeName.encode('utf-8'))

	def SetMustExist(self, bMustExist):
		lib.mdMUIncrementalSetMustExist(self.I, bMustExist)

	def SetKeyFile(self, KeyFile):
		lib.mdMUIncrementalSetKeyFile(self.I, KeyFile.encode('utf-8'))

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdMUIncrementalInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdMUIncrementalGetInitializeErrorString(self.I).decode('utf-8')

	def SetLicenseString(self, License):
		return lib.mdMUIncrementalSetLicenseString(self.I, License.encode('utf-8'))

	def SetMaximumCharacterSize(self, size):
		lib.mdMUIncrementalSetMaximumCharacterSize(self.I, size)

	def SetEncoding(self, encodeName):
		return lib.mdMUIncrementalSetEncoding(self.I, encodeName.encode('utf-8'))

	def GetBuildNumber(self):
		return lib.mdMUIncrementalGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdMUIncrementalGetDatabaseDate(self.I).decode('utf-8')

	def GetDatabaseExpirationDate(self):
		return lib.mdMUIncrementalGetDatabaseExpirationDate(self.I).decode('utf-8')

	def GetLicenseExpirationDate(self):
		return lib.mdMUIncrementalGetLicenseExpirationDate(self.I).decode('utf-8')

	def GetMatchcodeObject(self):
		return lib.mdMUIncrementalGetMatchcodeObject(self.I)

	def ClearMappings(self):
		lib.mdMUIncrementalClearMappings(self.I)

	def AddMapping(self, Mapping):
		return lib.mdMUIncrementalAddMapping(self.I, MatchcodeMapping(Mapping).value)

	def ClearFields(self):
		lib.mdMUIncrementalClearFields(self.I)

	def AddField(self, Field):
		lib.mdMUIncrementalAddField(self.I, Field.encode('utf-8'))

	def BuildKey(self):
		lib.mdMUIncrementalBuildKey(self.I)

	def SetKey(self, Key):
		lib.mdMUIncrementalSetKey(self.I, Key.encode('utf-8'))

	def SetUserInfo(self, UserInfo):
		lib.mdMUIncrementalSetUserInfo(self.I, UserInfo.encode('utf-8'))

	def MatchRecord(self):
		lib.mdMUIncrementalMatchRecord(self.I)

	def AddRecord(self):
		lib.mdMUIncrementalAddRecord(self.I)

	def NextMatchingRecord(self):
		return lib.mdMUIncrementalNextMatchingRecord(self.I)

	def GetKey(self):
		return lib.mdMUIncrementalGetKey(self.I).decode('utf-8')

	def GetUserInfo(self):
		return lib.mdMUIncrementalGetUserInfo(self.I).decode('utf-8')

	def GetDupeGroup(self):
		return lib.mdMUIncrementalGetDupeGroup(self.I)

	def GetStatusCode(self):
		return lib.mdMUIncrementalGetStatusCode(self.I).decode('utf-8')

	def GetCount(self):
		return lib.mdMUIncrementalGetCount(self.I)

	def GetEntry(self):
		return lib.mdMUIncrementalGetEntry(self.I)

	def GetCombinations(self):
		return lib.mdMUIncrementalGetCombinations(self.I)

	def GetResults(self):
		return lib.mdMUIncrementalGetResults(self.I).decode('utf-8')

	def GetFuzzyPercentage(self):
		return lib.mdMUIncrementalGetFuzzyPercentage(self.I)

	def SetReserved(self, Property, Value):
		lib.mdMUIncrementalSetReserved(self.I, Property.encode('utf-8'), Value.encode('utf-8'))

	def GetReserved(self, Property):
		return lib.mdMUIncrementalGetReserved(self.I, Property.encode('utf-8')).decode('utf-8')

	def BeginTransaction(self):
		return lib.mdMUIncrementalBeginTransaction(self.I)

	def CommitTransaction(self):
		return lib.mdMUIncrementalCommitTransaction(self.I)

	def RollbackTransaction(self):
		return lib.mdMUIncrementalRollbackTransaction(self.I)

# mdMUHybrid Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorConfigFile = 1
	ErrorLicenseExpired = 2
	ErrorDatabaseExpired = 3
	ErrorMatchcodeNotSpecified = 4
	ErrorMatchcodeNotFound = 5
	ErrorInvalidMatchcode = 6
	ErrorKeyFile = 7
	ErrorNoneIntersectingGroupCache = 8
	ErrorMatchcodeObsolete = 9
	ErrorGlobalAddrInit = 10
	ErrorIntlLicenseRequired = 11

class MatchcodeComponentType(Enum):
	PrefixComp = 1
	FirstComp = 2
	MiddleComp = 3
	LastComp = 4
	SuffixComp = 5
	GenderComp = 6
	FirstNicknameComp = 7
	MiddleNicknameComp = 8
	TitleComp = 9
	CompanyComp = 10
	CompanyAcronymComp = 11
	StreetNumberComp = 12
	StreetPreDirComp = 13
	StreetNameComp = 14
	StreetSuffixComp = 15
	StreetPostDirComp = 16
	POBoxComp = 17
	SecondaryComp = 18
	AddressComp = 19
	CityComp = 20
	StateComp = 21
	Zip9Comp = 22
	Zip5Comp = 23
	Zip4Comp = 24
	CountryComp = 28
	CanadianPCComp = 29
	PhoneComp = 33
	EMailComp = 34
	CreditCardComp = 35
	GeneralComp = 36
	GeoDistanceComp = 38
	DateComp = 39
	NumericComp = 40
	PremisesNumberComp = 41
	ThoroughfarePreDirComp = 42
	ThoroughfareLeadingTypeComp = 43
	ThoroughfareNameComp = 44
	ThoroughfarePostDirComp = 45
	ThoroughfareTrailingTypeComp = 46
	DepThoroughfarePreDirComp = 47
	DepThoroughfareLeadingTypeComp = 48
	DepThoroughfareNameComp = 49
	DepThoroughfarePostDirComp = 50
	DepThoroughfareTrailingTypeComp = 51
	LocalityComp = 52
	DependentLocalityComp = 53
	DblDependentLocalityComp = 54
	AdministrativeAreaComp = 55
	SubAdministrativeAreaComp = 56
	PostalCodeComp = 57
	SubNationalAreaComp = 58
	PostBoxComp = 59

class MatchcodeStart(Enum):
	Left = 8
	Right = 16
	StartAtPos = 32
	StartAtWord = 64

class MatchcodeTrim(Enum):
	LeftTrim = 2
	RightTrim = 4
	AllTrim = 6

class MatchcodeFuzzy(Enum):
	Exact = 0
	SoundEx = 1
	Phonetex = 2
	Containment = 4
	Frequency = 8
	FastNear = 16
	AccurateNear = 32
	VowelsOnly = 64
	ConsonantsOnly = 128
	AlphasOnly = 256
	NumericsOnly = 512
	FrequencyNear = 1024
	NGram = 2048
	Jaro = 4096
	JaroWinkler = 8192
	LCS = 16384
	NeedlemanWunsch = 32768
	MDKeyboard = 65536
	SmithWatermanGotoh = 131072
	Dice = 262144
	Jaccard = 524288
	Overlap = 1048576
	DoubleMetaphone = 2097152
	UTF8Near = 4194304

class MatchcodeFieldMatch(Enum):
	NoFieldMatch = 0
	BothBlankMatch = 256
	OneBlankMatch = 512
	InitialMatch = 1024

class MatchcodeSwap(Enum):
	NoSwap = 0
	SwapA = 1
	SwapB = 2
	SwapC = 4
	SwapD = 8
	SwapE = 16
	SwapF = 32
	SwapG = 64
	SwapH = 128
	BothA = 256
	BothB = 512
	BothC = 1024
	BothD = 2048
	BothE = 4096
	BothF = 8192
	BothG = 16384
	BothH = 32768

class MatchcodeCombination(Enum):
	Combo1 = 1
	Combo2 = 2
	Combo3 = 4
	Combo4 = 8
	Combo5 = 16
	Combo6 = 32
	Combo7 = 64
	Combo8 = 128
	Combo9 = 256
	Combo10 = 512
	Combo11 = 1024
	Combo12 = 2048
	Combo13 = 4096
	Combo14 = 8192
	Combo15 = 16384
	Combo16 = 32768

class MatchcodeMappingTarget(Enum):
	PrefixType = 1
	FirstType = 2
	MiddleType = 3
	LastType = 4
	SuffixType = 5
	GenderType = 6
	FirstNicknameType = 7
	MiddleNicknameType = 8
	TitleType = 9
	CompanyType = 10
	CompanyAcronymType = 11
	AddressType = 12
	CityType = 13
	StateType = 14
	Zip9Type = 15
	Zip5Type = 16
	Zip4Type = 17
	CountryType = 18
	CanadianPCType = 19
	PhoneType = 23
	EMailType = 24
	CreditCardType = 25
	GeneralType = 26
	Address1Type = 28
	Address2Type = 29
	Address3Type = 30
	LatitudeType = 34
	LongitudeType = 35
	DateType = 36
	NumericType = 37
	Address4Type = 38
	Address5Type = 39
	Address6Type = 40
	Address7Type = 41
	Address8Type = 42

class MatchcodeStatus(Enum):
	MCNoError = 0
	MCFirstComponentFuzzyOptions = 1
	MCFirstComponentNoSwapPair = 2
	MCDataTypeNoFuzzy = 3
	MCComponentFuzzyIncorrectSize = 4
	MCDataTypeNoMaximumNumberWords = 5
	MCDataTypeNoStartRightOrWordOrPos = 6
	MCIncorrectMaximumNumberWords = 7
	MCNearOutOfRange = 8
	MCFirstComponentNotUsedInEveryCondition = 9
	MCCannotChangeFirstComponent = 10
	MCInvalidSwapPair = 11
	MCIncorrectStartPosOrStartWord = 12
	MCInvalidMatchcodeComponentType = 13

class MatchcodeMapping(Enum):
	Prefix = 1
	Gender = 2
	First = 3
	MixedFirst = 4
	Middle = 5
	Last = 6
	MixedLast = 7
	Suffix = 8
	FullName = 9
	InverseName = 10
	GovernmentInverseName = 11
	Title = 12
	Company = 13
	Address = 14
	City = 15
	State = 16
	Zip9 = 17
	Zip5 = 18
	Zip4 = 19
	CityStZip = 20
	Country = 21
	CanadianPostalCode = 22
	Phone = 27
	EMail = 28
	CreditCard = 29
	General = 30
	Latitude = 40
	Longitude = 41
	Date = 42
	Numeric = 43

class MatchcodeNearType(Enum):
	NearNone = 0
	NearInteger = 1
	NearFloat = 2

class ComponentCountryType(Enum):
	US = 1
	Canada = 2
	Global = 4
	Domestic = 3

class mdMUHybrid(object):
	def __init__(self):
		self.I = lib.mdMUHybridCreate()

	def __del__(self):
		lib.mdMUHybridDestroy(self.I)

	def SetPathToMatchUpFiles(self, Path):
		lib.mdMUHybridSetPathToMatchUpFiles(self.I, Path.encode('utf-8'))

	def SetMatchcodeName(self, MatchcodeName):
		lib.mdMUHybridSetMatchcodeName(self.I, MatchcodeName.encode('utf-8'))

	def InitializeDataFiles(self):
		return ProgramStatus(lib.mdMUHybridInitializeDataFiles(self.I))

	def GetInitializeErrorString(self):
		return lib.mdMUHybridGetInitializeErrorString(self.I).decode('utf-8')

	def SetLicenseString(self, License):
		return lib.mdMUHybridSetLicenseString(self.I, License.encode('utf-8'))

	def SetMaximumCharacterSize(self, size):
		lib.mdMUHybridSetMaximumCharacterSize(self.I, size)

	def SetEncoding(self, encodeName):
		return lib.mdMUHybridSetEncoding(self.I, encodeName.encode('utf-8'))

	def GetBuildNumber(self):
		return lib.mdMUHybridGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdMUHybridGetDatabaseDate(self.I).decode('utf-8')

	def GetDatabaseExpirationDate(self):
		return lib.mdMUHybridGetDatabaseExpirationDate(self.I).decode('utf-8')

	def GetLicenseExpirationDate(self):
		return lib.mdMUHybridGetLicenseExpirationDate(self.I).decode('utf-8')

	def GetMatchcodeObject(self):
		return lib.mdMUHybridGetMatchcodeObject(self.I)

	def ClearMappings(self):
		lib.mdMUHybridClearMappings(self.I)

	def AddMapping(self, Mapping):
		return lib.mdMUHybridAddMapping(self.I, MatchcodeMapping(Mapping).value)

	def ClearFields(self):
		lib.mdMUHybridClearFields(self.I)

	def AddField(self, Field):
		lib.mdMUHybridAddField(self.I, Field.encode('utf-8'))

	def BuildKey(self):
		lib.mdMUHybridBuildKey(self.I)

	def GetKey(self):
		return lib.mdMUHybridGetKey(self.I).decode('utf-8')

	def GetKeySize(self):
		return lib.mdMUHybridGetKeySize(self.I)

	def GetClusterSize(self):
		return lib.mdMUHybridGetClusterSize(self.I)

	def CompareKeys(self, Key1, Key2):
		return lib.mdMUHybridCompareKeys(self.I, Key1.encode('utf-8'), Key2.encode('utf-8'))

	def GetResults(self):
		return lib.mdMUHybridGetResults(self.I).decode('utf-8')

	def GetFuzzyPercentage(self):
		return lib.mdMUHybridGetFuzzyPercentage(self.I)

	def SetReserved(self, Property, Value):
		lib.mdMUHybridSetReserved(self.I, Property.encode('utf-8'), Value.encode('utf-8'))

	def GetReserved(self, Property):
		return lib.mdMUHybridGetReserved(self.I, Property.encode('utf-8')).decode('utf-8')
