# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)]
# From type library 'ChemDrawBase.dll'
# On Thu Sep 17 19:56:29 2026
'CS ChemDraw 64-bit 22.0 Object Library'
makepy_version = '0.5.01'
python_version = 0x30d02f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{358D7CC8-6160-42DC-A9A3-E942D5325349}')
MajorVersion = 22
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	kCDAminoAcidHOH               =0          # from enum CDAminoAcidTermini
	kCDAminoAcidNH2COOH           =1          # from enum CDAminoAcidTermini
	kCDArrowHeadPositionFull      =2          # from enum CDArrowHeadPositionType
	kCDArrowHeadPositionHalfLeft  =3          # from enum CDArrowHeadPositionType
	kCDArrowHeadPositionHalfRight =4          # from enum CDArrowHeadPositionType
	kCDArrowHeadPositionNone      =1          # from enum CDArrowHeadPositionType
	kCDArrowHeadPositionUnspecified=0          # from enum CDArrowHeadPositionType
	kCDArrowHeadTypeAngle         =3          # from enum CDArrowHeadType
	kCDArrowHeadTypeHollow        =2          # from enum CDArrowHeadType
	kCDArrowHeadTypeSolid         =1          # from enum CDArrowHeadType
	kCDArrowHeadTypeUnspecified   =0          # from enum CDArrowHeadType
	kCDArrowTypeEquilibrium       =8          # from enum CDArrowType
	kCDArrowTypeFullHead          =2          # from enum CDArrowType
	kCDArrowTypeHalfHead          =1          # from enum CDArrowType
	kCDArrowTypeHollow            =16         # from enum CDArrowType
	kCDArrowTypeNoHead            =0          # from enum CDArrowType
	kCDArrowTypeResonance         =4          # from enum CDArrowType
	kCDArrowTypeRetroSynthetic    =32         # from enum CDArrowType
	kCDCIPAtomNone                =1          # from enum CDAtomCIPType
	kCDCIPAtomPseudoR             =4          # from enum CDAtomCIPType
	kCDCIPAtomPseudoS             =5          # from enum CDAtomCIPType
	kCDCIPAtomR                   =2          # from enum CDAtomCIPType
	kCDCIPAtomS                   =3          # from enum CDAtomCIPType
	kCDCIPAtomUndetermined        =0          # from enum CDAtomCIPType
	kCDCIPAtomUnspecified         =6          # from enum CDAtomCIPType
	kCDAtomGeometry10Ligand       =16         # from enum CDAtomGeometry
	kCDAtomGeometry1Ligand        =1          # from enum CDAtomGeometry
	kCDAtomGeometry5Ligand        =10         # from enum CDAtomGeometry
	kCDAtomGeometry6Ligand        =12         # from enum CDAtomGeometry
	kCDAtomGeometry7Ligand        =13         # from enum CDAtomGeometry
	kCDAtomGeometry8Ligand        =14         # from enum CDAtomGeometry
	kCDAtomGeometry9Ligand        =15         # from enum CDAtomGeometry
	kCDAtomGeometryBent           =3          # from enum CDAtomGeometry
	kCDAtomGeometryLinear         =2          # from enum CDAtomGeometry
	kCDAtomGeometryOctahedral     =11         # from enum CDAtomGeometry
	kCDAtomGeometrySquarePlanar   =6          # from enum CDAtomGeometry
	kCDAtomGeometrySquarePyramidal=9          # from enum CDAtomGeometry
	kCDAtomGeometryTetrahedral    =7          # from enum CDAtomGeometry
	kCDAtomGeometryTrigonalBipyramidal=8          # from enum CDAtomGeometry
	kCDAtomGeometryTrigonalPlanar =4          # from enum CDAtomGeometry
	kCDAtomGeometryTrigonalPyramidal=5          # from enum CDAtomGeometry
	kCDAtomGeometryUnknown        =0          # from enum CDAtomGeometry
	kCDAtomRestrictFreeSites      =1          # from enum CDAtomSubstituentType
	kCDAtomRestrictNone           =0          # from enum CDAtomSubstituentType
	kCDAtomRestrictSubstituentsExactly=3          # from enum CDAtomSubstituentType
	kCDAtomRestrictSubstituentsUpTo=2          # from enum CDAtomSubstituentType
	kCDCIPBondE                   =2          # from enum CDBondCIPType
	kCDCIPBondNone                =1          # from enum CDBondCIPType
	kCDCIPBondUndetermined        =0          # from enum CDBondCIPType
	kCDCIPBondZ                   =3          # from enum CDBondCIPType
	kCDBondDisplayBold            =5          # from enum CDBondDisplay
	kCDBondDisplayDash            =1          # from enum CDBondDisplay
	kCDBondDisplayHash            =2          # from enum CDBondDisplay
	kCDBondDisplayHollowWedgeBegin=9          # from enum CDBondDisplay
	kCDBondDisplayHollowWedgeEnd  =10         # from enum CDBondDisplay
	kCDBondDisplaySolid           =0          # from enum CDBondDisplay
	kCDBondDisplayWavy            =8          # from enum CDBondDisplay
	kCDBondDisplayWedgeBegin      =6          # from enum CDBondDisplay
	kCDBondDisplayWedgeEnd        =7          # from enum CDBondDisplay
	kCDBondDisplayWedgedHashBegin =3          # from enum CDBondDisplay
	kCDBondDisplayWedgedHashEnd   =4          # from enum CDBondDisplay
	kCDBondDoublePositionAutoCenter=0          # from enum CDBondDoublePosition
	kCDBondDoublePositionAutoLeft =2          # from enum CDBondDoublePosition
	kCDBondDoublePositionAutoRight=1          # from enum CDBondDoublePosition
	kCDBondDoublePositionUserCenter=256        # from enum CDBondDoublePosition
	kCDBondDoublePositionUserLeft =258        # from enum CDBondDoublePosition
	kCDBondDoublePositionUserRight=257        # from enum CDBondDoublePosition
	kCDBondOrderAny               =-1         # from enum CDBondOrder
	kCDBondOrderDative            =4096       # from enum CDBondOrder
	kCDBondOrderDouble            =2          # from enum CDBondOrder
	kCDBondOrderDoubleOrAromatic  =130        # from enum CDBondOrder
	kCDBondOrderFiveHalf          =2048       # from enum CDBondOrder
	kCDBondOrderFourHalf          =1024       # from enum CDBondOrder
	kCDBondOrderHalf              =64         # from enum CDBondOrder
	kCDBondOrderHydrogen          =16384      # from enum CDBondOrder
	kCDBondOrderIonic             =8192       # from enum CDBondOrder
	kCDBondOrderOneHalf           =128        # from enum CDBondOrder
	kCDBondOrderQuadruple         =8          # from enum CDBondOrder
	kCDBondOrderQuintuple         =16         # from enum CDBondOrder
	kCDBondOrderSextuple          =32         # from enum CDBondOrder
	kCDBondOrderSingle            =1          # from enum CDBondOrder
	kCDBondOrderSingleOrAromatic  =129        # from enum CDBondOrder
	kCDBondOrderSingleOrDouble    =3          # from enum CDBondOrder
	kCDBondOrderThreeCenter       =32768      # from enum CDBondOrder
	kCDBondOrderThreeHalf         =512        # from enum CDBondOrder
	kCDBondOrderTriple            =4          # from enum CDBondOrder
	kCDBondOrderTwoHalf           =256        # from enum CDBondOrder
	kCDBondReactionParticipationChangeType=3          # from enum CDBondReactionParticipation
	kCDBondReactionParticipationMakeAndChange=4          # from enum CDBondReactionParticipation
	kCDBondReactionParticipationMakeOrBreak=2          # from enum CDBondReactionParticipation
	kCDBondReactionParticipationNoChange=6          # from enum CDBondReactionParticipation
	kCDBondReactionParticipationNotReactionCenter=5          # from enum CDBondReactionParticipation
	kCDBondReactionParticipationReactionCenter=1          # from enum CDBondReactionParticipation
	kCDBondReactionParticipationUnmapped=7          # from enum CDBondReactionParticipation
	kCDBondReactionParticipationUnspecified=0          # from enum CDBondReactionParticipation
	kCDBondTopologyChain          =2          # from enum CDBondTopology
	kCDBondTopologyRing           =1          # from enum CDBondTopology
	kCDBondTopologyRingOrChain    =3          # from enum CDBondTopology
	kCDBondTopologyUnspecified    =0          # from enum CDBondTopology
	kCDBracketTypeCurly           =1          # from enum CDBracketType
	kCDBracketTypeRound           =2          # from enum CDBracketType
	kCDBracketTypeSquare          =0          # from enum CDBracketType
	kCDBracketUsageAnypolymer     =18         # from enum CDBracketUsage
	kCDBracketUsageComponent      =13         # from enum CDBracketUsage
	kCDBracketUsageCopolymer      =6          # from enum CDBracketUsage
	kCDBracketUsageCopolymerAlternating=7          # from enum CDBracketUsage
	kCDBracketUsageCopolymerBlock =9          # from enum CDBracketUsage
	kCDBracketUsageCopolymerRandom=8          # from enum CDBracketUsage
	kCDBracketUsageCrosslink      =10         # from enum CDBracketUsage
	kCDBracketUsageGeneric        =17         # from enum CDBracketUsage
	kCDBracketUsageGraft          =11         # from enum CDBracketUsage
	kCDBracketUsageMer            =5          # from enum CDBracketUsage
	kCDBracketUsageMixtureOrdered =15         # from enum CDBracketUsage
	kCDBracketUsageMixtureUnordered=14         # from enum CDBracketUsage
	kCDBracketUsageModification   =12         # from enum CDBracketUsage
	kCDBracketUsageMonomer        =4          # from enum CDBracketUsage
	kCDBracketUsageMultipleGroup  =16         # from enum CDBracketUsage
	kCDBracketUsageSRU            =3          # from enum CDBracketUsage
	kCDBracketUsageUnspecified    =0          # from enum CDBracketUsage
	kCDBracketUsageUnused1        =1          # from enum CDBracketUsage
	kCDBracketUsageUnused2        =2          # from enum CDBracketUsage
	kCDShowWarnAmbigStereo        =64         # from enum CDChemicalWarningTypes
	kCDShowWarnEnhancedStereo     =2048       # from enum CDChemicalWarningTypes
	kCDShowWarnHydrogenBonds      =1024       # from enum CDChemicalWarningTypes
	kCDShowWarnIsotopes           =4          # from enum CDChemicalWarningTypes
	kCDShowWarnLinearAtoms        =256        # from enum CDChemicalWarningTypes
	kCDShowWarnMisc               =512        # from enum CDChemicalWarningTypes
	kCDShowWarnParens             =2          # from enum CDChemicalWarningTypes
	kCDShowWarnStereoBtw          =128        # from enum CDChemicalWarningTypes
	kCDShowWarnStrayAtoms         =16         # from enum CDChemicalWarningTypes
	kCDShowWarnStrayBonds         =8          # from enum CDChemicalWarningTypes
	kCDShowWarnUndefinedStereo    =32         # from enum CDChemicalWarningTypes
	kCDShowWarnValence            =1          # from enum CDChemicalWarningTypes
	kCDConstraintTypeAngle        =2          # from enum CDConstraintType
	kCDConstraintTypeDistance     =1          # from enum CDConstraintType
	kCDConstraintTypeExclusionSphere=3          # from enum CDConstraintType
	kCDConstraintTypeUndefined    =0          # from enum CDConstraintType
	kCDDrawingSpacePages          =0          # from enum CDDrawingSpaceType
	kCDDrawingSpacePoster         =1          # from enum CDDrawingSpaceType
	kCDEPSBondQualityHigh         =1          # from enum CDEPSBondQuality
	kCDEPSBondQualitySimplified   =2          # from enum CDEPSBondQuality
	kCDEPSColorCMYK               =4          # from enum CDEPSColor
	kCDEPSColorGrayscale          =2          # from enum CDEPSColor
	kCDEPSColorMonochrome         =1          # from enum CDEPSColor
	kCDEPSColorRGB                =3          # from enum CDEPSColor
	kCDEnhancedStereoAbsolute     =2          # from enum CDEnhancedStereoType
	kCDEnhancedStereoAnd          =4          # from enum CDEnhancedStereoType
	kCDEnhancedStereoNone         =1          # from enum CDEnhancedStereoType
	kCDEnhancedStereoOr           =3          # from enum CDEnhancedStereoType
	kCDEnhancedStereoUnspecified  =0          # from enum CDEnhancedStereoType
	kCDExternalConnectionDiamond  =1          # from enum CDExternalConnectionType
	kCDExternalConnectionPolymerBead=3          # from enum CDExternalConnectionType
	kCDExternalConnectionStar     =2          # from enum CDExternalConnectionType
	kCDExternalConnectionUnspecified=0          # from enum CDExternalConnectionType
	kCDExternalConnectionWavy     =4          # from enum CDExternalConnectionType
	kCDXExternalConnectionResidue =5          # from enum CDExternalConnectionType
	kCDFillTypeFaded              =4          # from enum CDFillType
	kCDFillTypeNone               =1          # from enum CDFillType
	kCDFillTypeShaded             =3          # from enum CDFillType
	kCDFillTypeSolid              =2          # from enum CDFillType
	kCDFillTypeUnspecified        =0          # from enum CDFillType
	kCDFontStyleBold              =1          # from enum CDFontStyle
	kCDFontStyleFormula           =96         # from enum CDFontStyle
	kCDFontStyleItalic            =2          # from enum CDFontStyle
	kCDFontStyleOutline           =8          # from enum CDFontStyle
	kCDFontStylePlain             =0          # from enum CDFontStyle
	kCDFontStyleShadow            =16         # from enum CDFontStyle
	kCDFontStyleSubscript         =32         # from enum CDFontStyle
	kCDFontStyleSuperscript       =64         # from enum CDFontStyle
	kCDFontStyleUnderline         =4          # from enum CDFontStyle
	kCDFormatBMP                  =542133570  # from enum CDFormat
	kCDFormatCDX                  =1397573699 # from enum CDFormat
	kCDFormatCDXML                =1299735619 # from enum CDFormat
	kCDFormatCML                  =544634727  # from enum CDFormat
	kCDFormatChemDraw35           =892553283  # from enum CDFormat
	kCDFormatChemicalName         =1701658990 # from enum CDFormat
	kCDFormatConnTab              =1950573635 # from enum CDFormat
	kCDFormatEPSFPreview          =1347637317 # from enum CDFormat
	kCDFormatEPSFText             =1414746181 # from enum CDFormat
	kCDFormatEnhMetafile          =1279675717 # from enum CDFormat
	kCDFormatF1Query              =1363560515 # from enum CDFormat
	kCDFormatF1Structure          =826689603  # from enum CDFormat
	kCDFormatGIF                  =1715882311 # from enum CDFormat
	kCDFormatGalacticSpectra      =541282387  # from enum CDFormat
	kCDFormatHELM                 =1296844104 # from enum CDFormat
	kCDFormatISISReaction         =1314411117 # from enum CDFormat
	kCDFormatISISSketch           =1129010029 # from enum CDFormat
	kCDFormatISISTGF              =1179079789 # from enum CDFormat
	kCDFormatInChI                =1749249609 # from enum CDFormat
	kCDFormatJPEG                 =1195724874 # from enum CDFormat
	kCDFormatJcampSpectra         =542655562  # from enum CDFormat
	kCDFormatMDLMolfile           =1280265581 # from enum CDFormat
	kCDFormatMDLSDfile            =1178882925 # from enum CDFormat
	kCDFormatMSIChemNote          =1298756461 # from enum CDFormat
	kCDFormatMetafile             =1279675735 # from enum CDFormat
	kCDFormatPNG                  =1715949136 # from enum CDFormat
	kCDFormatSLN                  =2119060563 # from enum CDFormat
	kCDFormatSMD                  =1684886371 # from enum CDFormat
	kCDFormatSMILES               =2118733139 # from enum CDFormat
	kCDFormatTIFF                 =1179011412 # from enum CDFormat
	kCDFragmentationAnalyzerTypeCombinatorial=1          # from enum CDFragmentationAnalyzerType
	kCDFragmentationAnalyzerTypeSequential=2          # from enum CDFragmentationAnalyzerType
	kCDFragmentationAnalyzerTypeSimultaneous=3          # from enum CDFragmentationAnalyzerType
	kCDFragmentationAnalyzerTypeUnspecified=0          # from enum CDFragmentationAnalyzerType
	kCDFragmentationHighlightTypeFormula=2          # from enum CDFragmentationHighlightType
	kCDFragmentationHighlightTypeFragment=4          # from enum CDFragmentationHighlightType
	kCDFragmentationHighlightTypeMass=1          # from enum CDFragmentationHighlightType
	kCDFragmentationHighlightTypeUnspecified=0          # from enum CDFragmentationHighlightType
	kCDGeometryTypeCentroidFromPoints=7          # from enum CDGeometryType
	kCDGeometryTypeLineFromPoints =4          # from enum CDGeometryType
	kCDGeometryTypeNormalFromPointPlane=8          # from enum CDGeometryType
	kCDGeometryTypePlaneFromPointLine=6          # from enum CDGeometryType
	kCDGeometryTypePlaneFromPoints=5          # from enum CDGeometryType
	kCDGeometryTypePointFromPointNormalDistance=3          # from enum CDGeometryType
	kCDGeometryTypePointFromPointPointDistance=1          # from enum CDGeometryType
	kCDGeometryTypePointFromPointPointPercentage=2          # from enum CDGeometryType
	kCDGeometryTypeUndefined      =0          # from enum CDGeometryType
	kCDGraphicTypeArc             =2          # from enum CDGraphicType
	kCDGraphicTypeBracket         =6          # from enum CDGraphicType
	kCDGraphicTypeLine            =1          # from enum CDGraphicType
	kCDGraphicTypeOrbital         =5          # from enum CDGraphicType
	kCDGraphicTypeOval            =4          # from enum CDGraphicType
	kCDGraphicTypeRectangle       =3          # from enum CDGraphicType
	kCDGraphicTypeSymbol          =7          # from enum CDGraphicType
	kCDGraphicTypeUndefined       =0          # from enum CDGraphicType
	kCDGroupTypeFragment          =1          # from enum CDGroupType
	kCDGroupTypeGroup             =0          # from enum CDGroupType
	kCDIsotopicAbundanceAny       =1          # from enum CDIsotopicAbundance
	kCDIsotopicAbundanceDeficient =4          # from enum CDIsotopicAbundance
	kCDIsotopicAbundanceEnriched  =3          # from enum CDIsotopicAbundance
	kCDIsotopicAbundanceNatural   =2          # from enum CDIsotopicAbundance
	kCDIsotopicAbundanceNonnatural=5          # from enum CDIsotopicAbundance
	kCDIsotopicAbundanceUnspecified=0          # from enum CDIsotopicAbundance
	kCDJustificationAbove         =3          # from enum CDJustification
	kCDJustificationAuto          =5          # from enum CDJustification
	kCDJustificationBelow         =4          # from enum CDJustification
	kCDJustificationBestInitial   =6          # from enum CDJustification
	kCDJustificationCenter        =1          # from enum CDJustification
	kCDJustificationJustified     =2          # from enum CDJustification
	kCDJustificationLeft          =0          # from enum CDJustification
	kCDJustificationRight         =-1         # from enum CDJustification
	kCDLabelDisplayAbove          =4          # from enum CDLabelDisplay
	kCDLabelDisplayAuto           =0          # from enum CDLabelDisplay
	kCDLabelDisplayBelow          =5          # from enum CDLabelDisplay
	kCDLabelDisplayBestInitial    =6          # from enum CDLabelDisplay
	kCDLabelDisplayCenter         =2          # from enum CDLabelDisplay
	kCDLabelDisplayLeft           =1          # from enum CDLabelDisplay
	kCDLabelDisplayRight          =3          # from enum CDLabelDisplay
	kCDLineHeightAuto             =1          # from enum CDLineHeight
	kCDLineHeightFixedMinimum     =2          # from enum CDLineHeight
	kCDLineHeightVariable         =0          # from enum CDLineHeight
	kCDLineTypeBold               =2          # from enum CDLineType
	kCDLineTypeDashed             =1          # from enum CDLineType
	kCDLineTypeSolid              =0          # from enum CDLineType
	kCDLineTypeWavy               =4          # from enum CDLineType
	kCDNoGoTypeCross              =2          # from enum CDNoGoType
	kCDNoGoTypeHash               =3          # from enum CDNoGoType
	kCDNoGoTypeNone               =1          # from enum CDNoGoType
	kCDNoGoTypeUnspecified        =0          # from enum CDNoGoType
	kCDNodeTypeAnonymousAlternativeGroup=8          # from enum CDNodeType
	kCDNodeTypeElement            =1          # from enum CDNodeType
	kCDNodeTypeElementList        =2          # from enum CDNodeType
	kCDNodeTypeElementListNickname=3          # from enum CDNodeType
	kCDNodeTypeExternalConnectionPoint=12         # from enum CDNodeType
	kCDNodeTypeFormula            =6          # from enum CDNodeType
	kCDNodeTypeFragment           =5          # from enum CDNodeType
	kCDNodeTypeGenericNickname    =7          # from enum CDNodeType
	kCDNodeTypeLinkNode           =13         # from enum CDNodeType
	kCDNodeTypeMultiAttachment    =10         # from enum CDNodeType
	kCDNodeTypeNamedAlternativeGroup=9          # from enum CDNodeType
	kCDNodeTypeNickname           =4          # from enum CDNodeType
	kCDNodeTypeUnspecified        =0          # from enum CDNodeType
	kCDNodeTypeVariableAttachment =11         # from enum CDNodeType
	kCDObjectTagTypeDouble        =1          # from enum CDObjectTagType
	kCDObjectTagTypeLong          =2          # from enum CDObjectTagType
	kCDObjectTagTypeString        =3          # from enum CDObjectTagType
	kCDObjectTagTypeUndefined     =0          # from enum CDObjectTagType
	kCDOrbitalTypedxy             =8          # from enum CDOrbitalType
	kCDOrbitalTypedxyFilled       =520        # from enum CDOrbitalType
	kCDOrbitalTypedz2Minus        =7          # from enum CDOrbitalType
	kCDOrbitalTypedz2MinusFilled  =519        # from enum CDOrbitalType
	kCDOrbitalTypedz2Plus         =6          # from enum CDOrbitalType
	kCDOrbitalTypedz2PlusFilled   =518        # from enum CDOrbitalType
	kCDOrbitalTypehybridMinus     =5          # from enum CDOrbitalType
	kCDOrbitalTypehybridMinusFilled=517        # from enum CDOrbitalType
	kCDOrbitalTypehybridPlus      =4          # from enum CDOrbitalType
	kCDOrbitalTypehybridPlusFilled=516        # from enum CDOrbitalType
	kCDOrbitalTypelobe            =2          # from enum CDOrbitalType
	kCDOrbitalTypelobeFilled      =514        # from enum CDOrbitalType
	kCDOrbitalTypelobeShaded      =258        # from enum CDOrbitalType
	kCDOrbitalTypeoval            =1          # from enum CDOrbitalType
	kCDOrbitalTypeovalFilled      =513        # from enum CDOrbitalType
	kCDOrbitalTypeovalShaded      =257        # from enum CDOrbitalType
	kCDOrbitalTypep               =3          # from enum CDOrbitalType
	kCDOrbitalTypepFilled         =515        # from enum CDOrbitalType
	kCDOrbitalTypepShaded         =259        # from enum CDOrbitalType
	kCDOrbitalTypes               =0          # from enum CDOrbitalType
	kCDOrbitalTypesFilled         =512        # from enum CDOrbitalType
	kCDOrbitalTypesShaded         =256        # from enum CDOrbitalType
	kCDOvalTypeBold               =16         # from enum CDOvalType
	kCDOvalTypeCircle             =1          # from enum CDOvalType
	kCDOvalTypeDashed             =8          # from enum CDOvalType
	kCDOvalTypeFaded              =48         # from enum CDOvalType
	kCDOvalTypeFilled             =4          # from enum CDOvalType
	kCDOvalTypeShaded             =2          # from enum CDOvalType
	kCDOvalTypeShadowed           =32         # from enum CDOvalType
	kCDPictureTypeExternal        =1          # from enum CDPictureType
	kCDPictureTypeOLE             =2          # from enum CDPictureType
	kCDPictureTypeSpectrum        =3          # from enum CDPictureType
	kCDPictureTypeUnknown         =0          # from enum CDPictureType
	kCDPolymerFlipTypeFlip        =2          # from enum CDPolymerFlipType
	kCDPolymerFlipTypeNoFlip      =1          # from enum CDPolymerFlipType
	kCDPolymerFlipTypeUnspecified =0          # from enum CDPolymerFlipType
	kCDPolymerRepeatPatternEitherUnknown=2          # from enum CDPolymerRepeatPattern
	kCDPolymerRepeatPatternHeadToHead=1          # from enum CDPolymerRepeatPattern
	kCDPolymerRepeatPatternHeadToTail=0          # from enum CDPolymerRepeatPattern
	kCDPositioningTypeAbsolute    =3          # from enum CDPositioningType
	kCDPositioningTypeAngle       =1          # from enum CDPositioningType
	kCDPositioningTypeAuto        =0          # from enum CDPositioningType
	kCDPositioningTypeOffset      =2          # from enum CDPositioningType
	kCDOpenToolBond               =3          # from enum CDPrefToolEnum
	kCDOpenToolLasso              =1          # from enum CDPrefToolEnum
	kCDOpenToolLast               =0          # from enum CDPrefToolEnum
	kCDOpenToolMarquee            =2          # from enum CDPrefToolEnum
	kCDRadicalDoublet             =2          # from enum CDRadical
	kCDRadicalNone                =0          # from enum CDRadical
	kCDRadicalSinglet             =1          # from enum CDRadical
	kCDRadicalTriplet             =3          # from enum CDRadical
	kCDReactionSchemeTypeBranched =8          # from enum CDReactionSchemeType
	kCDReactionSchemeTypeCircular =16         # from enum CDReactionSchemeType
	kCDReactionSchemeTypeEmpty    =1          # from enum CDReactionSchemeType
	kCDReactionSchemeTypeLinear   =4          # from enum CDReactionSchemeType
	kCDReactionSchemeTypePoint    =2          # from enum CDReactionSchemeType
	kCDReactionSchemeTypeUnspecified=0          # from enum CDReactionSchemeType
	kCDReactionStereoInversion    =1          # from enum CDReactionStereo
	kCDReactionStereoRetention    =2          # from enum CDReactionStereo
	kCDReactionStereoUnspecified  =0          # from enum CDReactionStereo
	kCDRectangleTypeBold          =32         # from enum CDRectangleType
	kCDRectangleTypeDashed        =16         # from enum CDRectangleType
	kCDRectangleTypeFaded         =48         # from enum CDRectangleType
	kCDRectangleTypeFilled        =8          # from enum CDRectangleType
	kCDRectangleTypePlain         =0          # from enum CDRectangleType
	kCDRectangleTypeRoundEdge     =1          # from enum CDRectangleType
	kCDRectangleTypeShaded        =4          # from enum CDRectangleType
	kCDRectangleTypeShadow        =2          # from enum CDRectangleType
	kCDRingBondCountAsDrawn       =1          # from enum CDRingBondCount
	kCDRingBondCountFusion        =3          # from enum CDRingBondCount
	kCDRingBondCountNoRingBonds   =0          # from enum CDRingBondCount
	kCDRingBondCountSimpleRing    =2          # from enum CDRingBondCount
	kCDRingBondCountSpiroOrHigher =4          # from enum CDRingBondCount
	kCDRingBondCountUnspecified   =-1         # from enum CDRingBondCount
	kCDGroupTypeDNA               =3          # from enum CDSequenceType
	kCDGroupTypePeptide1          =1          # from enum CDSequenceType
	kCDGroupTypePeptide3          =2          # from enum CDSequenceType
	kCDGroupTypeRNA               =4          # from enum CDSequenceType
	kCDGroupTypeUnknown           =0          # from enum CDSequenceType
	kCDSplineTypeArEnd            =8          # from enum CDSplineType
	kCDSplineTypeArStart          =16         # from enum CDSplineType
	kCDSplineTypeBold             =4          # from enum CDSplineType
	kCDSplineTypeClosed           =1          # from enum CDSplineType
	kCDSplineTypeDashed           =2          # from enum CDSplineType
	kCDSplineTypeDoubled          =512        # from enum CDSplineType
	kCDSplineTypeFilled           =128        # from enum CDSplineType
	kCDSplineTypeHArEnd           =32         # from enum CDSplineType
	kCDSplineTypeHArStart         =64         # from enum CDSplineType
	kCDSplineTypeOpen             =0          # from enum CDSplineType
	kCDSplineTypeShaded           =256        # from enum CDSplineType
	kCDSymbolTypeAbsolute         =11         # from enum CDSymbolType
	kCDSymbolTypeCircleMinus      =5          # from enum CDSymbolType
	kCDSymbolTypeCirclePlus       =4          # from enum CDSymbolType
	kCDSymbolTypeDagger           =6          # from enum CDSymbolType
	kCDSymbolTypeDoubleDagger     =7          # from enum CDSymbolType
	kCDSymbolTypeElectron         =1          # from enum CDSymbolType
	kCDSymbolTypeLonePair         =0          # from enum CDSymbolType
	kCDSymbolTypeMinus            =9          # from enum CDSymbolType
	kCDSymbolTypePlus             =8          # from enum CDSymbolType
	kCDSymbolTypeRacemic          =10         # from enum CDSymbolType
	kCDSymbolTypeRadicalAnion     =3          # from enum CDSymbolType
	kCDSymbolTypeRadicalCation    =2          # from enum CDSymbolType
	kCDSymbolTypeRelative         =12         # from enum CDSymbolType
	kCDTIFFColorCMYKContiguous    =4          # from enum CDTIFFColor
	kCDTIFFColorCMYKPlanar        =3          # from enum CDTIFFColor
	kCDTIFFColorMonochrome        =1          # from enum CDTIFFColor
	kCDTIFFColorRGB24             =2          # from enum CDTIFFColor
	kCDTIFFCompressionCCITT3      =3          # from enum CDTIFFCompression
	kCDTIFFCompressionCCITT4      =4          # from enum CDTIFFCompression
	kCDTIFFCompressionDeflate     =5          # from enum CDTIFFCompression
	kCDTIFFCompressionNone        =1          # from enum CDTIFFCompression
	kCDTIFFCompressionPackBits    =2          # from enum CDTIFFCompression
	kCDTranslationAny             =3          # from enum CDTranslation
	kCDTranslationBroad           =1          # from enum CDTranslation
	kCDTranslationEqual           =0          # from enum CDTranslation
	kCDTranslationNarrow          =2          # from enum CDTranslation
	kCDUnitCM                     =2          # from enum CDUnits
	kCDUnitInches                 =1          # from enum CDUnits
	kCDUnitPicas                  =4          # from enum CDUnits
	kCDUnitPoints                 =3          # from enum CDUnits
	kCDUnsaturationMustBeAbsent   =1          # from enum CDUnsaturation
	kCDUnsaturationMustBePresent  =2          # from enum CDUnsaturation
	kCDUnsaturationUnspecified    =0          # from enum CDUnsaturation
	kCOMenuItem                   =0          # from enum COCommandItemType
	kCOPopupMenu                  =1          # from enum COCommandItemType
	kCOAccessDenied               =1002       # from enum COErrors
	kCOEmpty                      =1003       # from enum COErrors
	kCONotSupported               =1005       # from enum COErrors
	kCOTypeMismatch               =1001       # from enum COErrors
	kCOUnknown                    =1004       # from enum COErrors
	vbCFBitmap                    =2          # from enum ClipBoardConstants
	vbCFDIB                       =8          # from enum ClipBoardConstants
	vbCFEMetafile                 =14         # from enum ClipBoardConstants
	vbCFFiles                     =15         # from enum ClipBoardConstants
	vbCFLink                      =-16640     # from enum ClipBoardConstants
	vbCFMetafile                  =3          # from enum ClipBoardConstants
	vbCFPalette                   =9          # from enum ClipBoardConstants
	vbCFRTF                       =-16639     # from enum ClipBoardConstants
	vbCFText                      =1          # from enum ClipBoardConstants

from win32com.client import DispatchBaseClass
class DataObject(DispatchBaseClass):
	'The DataObject object is used for specifying formats and data that will be supported for OLE drag and drop operations.'
	CLSID = IID('{41A7D760-6018-11CF-9016-00AA0068841E}')
	coclass_clsid = None

	def Clear(self):
		'Clears all data and formats in a DataObject object.'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	def GetData(self, Format=defaultNamedNotOptArg):
		'Retrieves data of a specified format from a DataObject object.'
		return self._ApplyTypes_(3, 1, (12, 0), ((3, 1),), 'GetData', None,Format
			)

	def GetFormat(self, Format=defaultNamedNotOptArg):
		'Determines if a specified clipboard format is supported by the DataObject object.'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (11, 0), ((3, 1),),Format
			)

	def SetData(self, Value=defaultNamedOptArg, Format=defaultNamedOptArg):
		'Adds a supported format and possibly its data to a DataObject object.'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((12, 17), (12, 17)),Value
			, Format)

	_prop_map_get_ = {
		# Method 'Files' returns object of type 'DataObjectFiles'
		"Files": (5, 2, (9, 0), (), "Files", '{41A7D761-6018-11CF-9016-00AA0068841E}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class DataObjectFiles(DispatchBaseClass):
	'The DataObjectFiles object is a collection of filenames used by the DataObject object (vbCFFiles format only).'
	CLSID = IID('{41A7D761-6018-11CF-9016-00AA0068841E}')
	coclass_clsid = None

	def Add(self, Filename=defaultNamedNotOptArg, index=defaultNamedOptArg):
		'Adds a filename to the Files collection of a DataObject object (vbCFFiles format only).'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (12, 17)),Filename
			, index)

	def Clear(self):
		'Clears all filenames stored in the Files collection of a DataObject object (vbCFFiles format only).'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), (),)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns a specific filename by index from the Files collection of a DataObject object (vbCFFiles format only).'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 2, (8, 0), ((3, 1),),index
			)

	def Remove(self, index=defaultNamedNotOptArg):
		'Removes a filename from the Files collection of a DataObject object (vbCFFiles format only).'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((12, 1),),index
			)

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Returns a specific filename by index from the Files collection of a DataObject object (vbCFFiles format only).'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(0, LCID, 2, (8, 0), ((3, 1),),index
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,1,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawAltGroup(DispatchBaseClass):
	'ChemDraw alternative group interface'
	CLSID = IID('{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')
	coclass_clsid = IID('{3CA7EAEC-2ED5-4E60-8261-D60CAA24F975}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'AltGroups' returns object of type 'IChemDrawAltGroups'
		"AltGroups": (309, 2, (9, 0), (), "AltGroups", '{D9E5D3D1-0D59-4126-B108-7D567E396FB3}'),
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'Arrows' returns object of type 'IChemDrawArrows'
		"Arrows": (316, 2, (9, 0), (), "Arrows", '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}'),
		# Method 'Atoms' returns object of type 'IChemDrawAtoms'
		"Atoms": (301, 2, (9, 0), (), "Atoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'Bonds' returns object of type 'IChemDrawBonds'
		"Bonds": (302, 2, (9, 0), (), "Bonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		# Method 'Brackets' returns object of type 'IChemDrawBrackets'
		"Brackets": (320, 2, (9, 0), (), "Brackets", '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}'),
		# Method 'Captions' returns object of type 'IChemDrawTexts'
		"Captions": (305, 2, (9, 0), (), "Captions", '{D156092E-1412-458C-BD6A-3CC171B56E63}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Constraints' returns object of type 'IChemDrawConstraints'
		"Constraints": (311, 2, (9, 0), (), "Constraints", '{990C82BE-55F2-49F2-B822-2E448C7FEC80}'),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Geometries' returns object of type 'IChemDrawGeometries'
		"Geometries": (310, 2, (9, 0), (), "Geometries", '{53C77081-53BF-4397-9BB4-84D6AF7C10F3}'),
		# Method 'Graphics' returns object of type 'IChemDrawGraphics'
		"Graphics": (303, 2, (9, 0), (), "Graphics", '{D0E3D4B9-3B16-4331-BBA2-651319AE0402}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'GroupFrame' returns object of type 'IChemDrawRect'
		"GroupFrame": (104, 2, (9, 0), (), "GroupFrame", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		# Method 'Groups' returns object of type 'IChemDrawGroups'
		"Groups": (307, 2, (9, 0), (), "Groups", '{E5164832-7AFC-463A-9C19-A1AF6D191020}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		# Method 'Objects' returns object of type 'IChemDrawObjects'
		"Objects": (101, 2, (9, 0), (), "Objects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Pictures' returns object of type 'IChemDrawPictures'
		"Pictures": (306, 2, (9, 0), (), "Pictures", '{41652842-15D6-44AE-AEFF-B51B179CF019}'),
		# Method 'PlasmidMaps' returns object of type 'IChemDrawPlasmidMaps'
		"PlasmidMaps": (315, 2, (9, 0), (), "PlasmidMaps", '{E06B3507-3060-4095-8406-BAADD00A054E}'),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'ReactionSchemes' returns object of type 'IChemDrawReactionSchemes'
		"ReactionSchemes": (312, 2, (9, 0), (), "ReactionSchemes", '{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		# Method 'Splines' returns object of type 'IChemDrawSplines'
		"Splines": (304, 2, (9, 0), (), "Splines", '{272423F1-2909-4340-8870-8062530ADD05}'),
		# Method 'StoichiometryGrids' returns object of type 'IChemDrawStoichiometryGrids'
		"StoichiometryGrids": (314, 2, (9, 0), (), "StoichiometryGrids", '{27109627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Symbols' returns object of type 'IChemDrawSymbols'
		"Symbols": (319, 2, (9, 0), (), "Symbols", '{D44C587D-2434-46B8-8B76-D309A2632456}'),
		# Method 'TLCPlates' returns object of type 'IChemDrawTLCPlates'
		"TLCPlates": (313, 2, (9, 0), (), "TLCPlates", '{27609627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Tables' returns object of type 'IChemDrawTables'
		"Tables": (308, 2, (9, 0), (), "Tables", '{80C78566-D4BF-460E-B055-5728877FB30E}'),
		# Method 'TextFrame' returns object of type 'IChemDrawRect'
		"TextFrame": (103, 2, (9, 0), (), "TextFrame", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		# Method 'caption' returns object of type 'IChemDrawText'
		"caption": (102, 2, (9, 0), (), "caption", '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}'),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"GroupFrame": ((104, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"TextFrame": ((103, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawAltGroups(DispatchBaseClass):
	'ChemDraw alternative groups interface'
	CLSID = IID('{D9E5D3D1-0D59-4126-B108-7D567E396FB3}')
	coclass_clsid = IID('{823B2C7E-8DC5-49BF-9FF1-F24F32A0B7AB}')

	# Result is of type IChemDrawAltGroup
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawAnnotation(DispatchBaseClass):
	'ChemDraw annotation interface'
	CLSID = IID('{DBD6A772-8979-4049-A58A-AA8F5D56A779}')
	coclass_clsid = IID('{DC1684DE-6A24-43AD-900C-BCE5150BB1F6}')

	_prop_map_get_ = {
		"Content": (102, 2, (8, 0), (), "Content", None),
		"Keyword": (101, 2, (8, 0), (), "Keyword", None),
	}
	_prop_map_put_ = {
		"Content": ((102, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawAnnotations(DispatchBaseClass):
	'ChemDraw annotations interface'
	CLSID = IID('{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}')
	coclass_clsid = IID('{AABDCC57-9D7B-4C81-9390-5703015A09E3}')

	def Add(self, Keyword=defaultNamedNotOptArg, Content=defaultNamedNotOptArg):
		'Create a new annotation with the specified keyword and content (will overwrite an existing annotation with the same keyword, if present)'
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((8, 1), (8, 1)),Keyword
			, Content)

	# Result is of type IChemDrawAnnotation
	def GetAnnotation(self, Keyword=defaultNamedNotOptArg):
		'Given an index or keyword, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(1610743815, LCID, 1, (9, 0), ((8, 1),),Keyword
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAnnotation', '{DBD6A772-8979-4049-A58A-AA8F5D56A779}')
		return ret

	# Result is of type IChemDrawAnnotation
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index or keyword, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DBD6A772-8979-4049-A58A-AA8F5D56A779}')
		return ret

	def Remove(self, Keyword=defaultNamedNotOptArg):
		'Remove the annotation with the given keyword'
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (24, 0), ((8, 1),),Keyword
			)

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index or keyword, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DBD6A772-8979-4049-A58A-AA8F5D56A779}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DBD6A772-8979-4049-A58A-AA8F5D56A779}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawApplication(DispatchBaseClass):
	'IChemDrawApplication interface'
	CLSID = IID('{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}')
	coclass_clsid = IID('{C172F840-938F-4A55-A732-4A036E3FBF3D}')

	def Quit(self):
		'Exits the application.'
		return self._oleobj_.InvokeTypes(1610743820, LCID, 1, (24, 0), (),)

	def UpdateRunLevel(self, progLevel=defaultNamedNotOptArg):
		'method UpdateRunLevel'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((12, 0),),progLevel
			)

	_prop_map_get_ = {
		# Method 'ActiveDocument' returns object of type 'IChemDrawDocument'
		"ActiveDocument": (1, 2, (9, 0), (), "ActiveDocument", '{9E3A4685-0A8F-420D-A73E-4A37B83830DB}'),
		# Method 'Application' returns object of type 'IChemDrawApplication'
		"Application": (2, 2, (9, 0), (), "Application", '{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}'),
		# Method 'DefaultDataType' returns object of type 'IChemDrawDataType'
		"DefaultDataType": (11, 2, (9, 0), (), "DefaultDataType", '{BB42A8EF-A444-40C2-BF4F-E156341E4127}'),
		# Method 'Documents' returns object of type 'IChemDrawDocuments'
		"Documents": (3, 2, (9, 0), (), "Documents", '{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}'),
		# Method 'ExportDataTypes' returns object of type 'IChemDrawDataTypes'
		"ExportDataTypes": (13, 2, (9, 0), (), "ExportDataTypes", '{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}'),
		"FullName": (4, 2, (8, 0), (), "FullName", None),
		# Method 'IODataTypes' returns object of type 'IChemDrawDataTypes'
		"IODataTypes": (14, 2, (9, 0), (), "IODataTypes", '{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}'),
		# Method 'ImportDataTypes' returns object of type 'IChemDrawDataTypes'
		"ImportDataTypes": (12, 2, (9, 0), (), "ImportDataTypes", '{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}'),
		"MainWindow": (9, 2, (20, 0), (), "MainWindow", None),
		# Method 'MenuBars' returns object of type 'IChemOfficeMenuBars'
		"MenuBars": (7, 2, (9, 0), (), "MenuBars", '{86BE5C00-1B92-11D0-87CF-1020AFD1F1AF}'),
		# Method 'Parent' returns object of type 'IChemDrawApplication'
		"Parent": (5, 2, (9, 0), (), "Parent", '{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}'),
		# Method 'Preferences' returns object of type 'IChemDrawPreferences'
		"Preferences": (8, 2, (9, 0), (), "Preferences", '{4BC8155A-553E-4992-A555-FEEECB11CAB8}'),
		"Visible": (6, 2, (11, 0), (), "Visible", None),
		"name": (0, 2, (8, 0), (), "name", None),
	}
	_prop_map_put_ = {
		"DefaultDataType": ((11, LCID, 4, 0),()),
		"Visible": ((6, LCID, 4, 0),()),
	}
	# Default property for this class is 'name'
	def __call__(self):
		return self._ApplyTypes_(*(0, 2, (8, 0), (), "name", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawArrow(DispatchBaseClass):
	'ChemDraw arrow and line object interface'
	CLSID = IID('{669C0868-90B0-4469-9621-7639880698B1}')
	coclass_clsid = IID('{E0D25ABD-8210-4390-AF26-EC7B85C651FA}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		"AngularSize": (113, 2, (5, 0), (), "AngularSize", None),
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'ArcOrigin' returns object of type 'IChemDrawPoint'
		"ArcOrigin": (122, 2, (9, 0), (), "ArcOrigin", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"ArrowHeadPositionStart": (105, 2, (3, 0), (), "ArrowHeadPositionStart", None),
		"ArrowHeadPositionTail": (106, 2, (3, 0), (), "ArrowHeadPositionTail", None),
		"ArrowHeadType": (104, 2, (3, 0), (), "ArrowHeadType", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'End' returns object of type 'IChemDrawPoint'
		"End": (102, 2, (9, 0), (), "End", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"EquilibriumRatio": (117, 2, (5, 0), (), "EquilibriumRatio", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"HeadCenterSize": (114, 2, (5, 0), (), "HeadCenterSize", None),
		"HeadSize": (112, 2, (5, 0), (), "HeadSize", None),
		"HeadWidth": (115, 2, (5, 0), (), "HeadWidth", None),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"IsArc": (107, 2, (11, 0), (), "IsArc", None),
		"IsBold": (110, 2, (11, 0), (), "IsBold", None),
		"IsDashed": (111, 2, (11, 0), (), "IsDashed", None),
		"IsDipole": (120, 2, (11, 0), (), "IsDipole", None),
		"IsLine": (109, 2, (11, 0), (), "IsLine", None),
		"IsNoGo": (119, 2, (11, 0), (), "IsNoGo", None),
		"IsStraightArrow": (108, 2, (11, 0), (), "IsStraightArrow", None),
		"IsWavy": (118, 2, (11, 0), (), "IsWavy", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"LineType": (103, 2, (3, 0), (), "LineType", None),
		"NoGoType": (121, 2, (3, 0), (), "NoGoType", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"ShaftSpacing": (116, 2, (5, 0), (), "ShaftSpacing", None),
		# Method 'Start' returns object of type 'IChemDrawPoint'
		"Start": (101, 2, (9, 0), (), "Start", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"AngularSize": ((113, LCID, 4, 0),()),
		"ArcOrigin": ((122, LCID, 4, 0),()),
		"ArrowHeadPositionStart": ((105, LCID, 4, 0),()),
		"ArrowHeadPositionTail": ((106, LCID, 4, 0),()),
		"ArrowHeadType": ((104, LCID, 4, 0),()),
		"Color": ((5, LCID, 4, 0),()),
		"End": ((102, LCID, 4, 0),()),
		"EquilibriumRatio": ((117, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"HeadCenterSize": ((114, LCID, 4, 0),()),
		"HeadSize": ((112, LCID, 4, 0),()),
		"HeadWidth": ((115, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"IsBold": ((110, LCID, 4, 0),()),
		"IsDashed": ((111, LCID, 4, 0),()),
		"IsDipole": ((120, LCID, 4, 0),()),
		"IsWavy": ((118, LCID, 4, 0),()),
		"LineType": ((103, LCID, 4, 0),()),
		"NoGoType": ((121, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"ShaftSpacing": ((116, LCID, 4, 0),()),
		"Start": ((101, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawArrows(DispatchBaseClass):
	'ChemDraw arrow and line objects interface'
	CLSID = IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')
	coclass_clsid = IID('{54B822AD-CD66-452E-A985-F7A78AD09987}')

	# Result is of type IChemDrawArrow
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{669C0868-90B0-4469-9621-7639880698B1}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{669C0868-90B0-4469-9621-7639880698B1}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{669C0868-90B0-4469-9621-7639880698B1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawAtom(DispatchBaseClass):
	'ChemDraw atom interface'
	CLSID = IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')
	coclass_clsid = IID('{2529F00D-9844-4F38-BDEB-6F59CFB816D7}')

	def AddAttachedAtom(self, pVal=defaultNamedNotOptArg):
		'Adds an atom to the collection of attached atoms, for multi-center atoms and variable attachment points.'
		return self._oleobj_.InvokeTypes(109, LCID, 1, (24, 0), ((9, 1),),pVal
			)

	def AddMappedAtom(self, pVal=defaultNamedNotOptArg):
		'Adds an atom to the collection of mapped atoms, for atom-atom mapping in reactions.'
		return self._oleobj_.InvokeTypes(130, LCID, 1, (24, 0), ((9, 1),),pVal
			)

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	def DeleteMapping(self):
		'Removes an atom from the collection of mapped atoms, for atom-atom mapping in reactions.'
		return self._oleobj_.InvokeTypes(131, LCID, 1, (24, 0), (),)

	def ExpandLabelToStructure(self):
		'Expand atom label to explicitly show the structure.'
		return self._oleobj_.InvokeTypes(141, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	def RemoveAttachedAtom(self, pVal=defaultNamedNotOptArg):
		'Removes an atom from the collection of attached atoms, for multi-center atoms and variable attachment points.'
		return self._oleobj_.InvokeTypes(110, LCID, 1, (24, 0), ((9, 1),),pVal
			)

	_prop_map_get_ = {
		"AbnormalValenceAllowed": (124, 2, (11, 0), (), "AbnormalValenceAllowed", None),
		# Method 'AlternativeGroup' returns object of type 'IChemDrawAltGroup'
		"AlternativeGroup": (128, 2, (9, 0), (), "AlternativeGroup", '{D300E59D-D1B4-42D0-9112-730BDBA31EF2}'),
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"AtomGeometry": (115, 2, (3, 0), (), "AtomGeometry", None),
		"AtomNumber": (114, 2, (8, 0), (), "AtomNumber", None),
		# Method 'AttachedAtoms' returns object of type 'IChemDrawAtoms'
		"AttachedAtoms": (108, 2, (9, 0), (), "AttachedAtoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		"AttachmentPointType": (140, 2, (3, 0), (), "AttachmentPointType", None),
		# Method 'Bonds' returns object of type 'IChemDrawBonds'
		"Bonds": (132, 2, (9, 0), (), "Bonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"Charge": (103, 2, (5, 0), (), "Charge", None),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		"ElementNumber": (102, 2, (3, 0), (), "ElementNumber", None),
		"EnhancedStereoGroupNumber": (143, 2, (3, 0), (), "EnhancedStereoGroupNumber", None),
		"EnhancedStereoType": (142, 2, (3, 0), (), "EnhancedStereoType", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"ImplicitHydrogensAllowed": (123, 2, (11, 0), (), "ImplicitHydrogensAllowed", None),
		"IsAttachmentPoint": (136, 2, (11, 0), (), "IsAttachmentPoint", None),
		"IsHDash": (112, 2, (11, 0), (), "IsHDash", None),
		"IsHDot": (111, 2, (11, 0), (), "IsHDot", None),
		"IsMultiCenter": (137, 2, (11, 0), (), "IsMultiCenter", None),
		"IsVariableAttach": (138, 2, (11, 0), (), "IsVariableAttach", None),
		"Isotope": (105, 2, (3, 0), (), "Isotope", None),
		"IsotopicAbundance": (122, 2, (3, 0), (), "IsotopicAbundance", None),
		"LabelDisplay": (107, 2, (3, 0), (), "LabelDisplay", None),
		"LabelText": (139, 2, (8, 0), (), "LabelText", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"LinkCountHigh": (127, 2, (3, 0), (), "LinkCountHigh", None),
		"LinkCountLow": (126, 2, (3, 0), (), "LinkCountLow", None),
		# Method 'MappedAtoms' returns object of type 'IChemDrawAtoms'
		"MappedAtoms": (129, 2, (9, 0), (), "MappedAtoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		"NodeType": (101, 2, (3, 0), (), "NodeType", None),
		"NumImplicitHydrogens": (106, 2, (3, 0), (), "NumImplicitHydrogens", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Radical": (104, 2, (3, 0), (), "Radical", None),
		"ReactionStereo": (120, 2, (3, 0), (), "ReactionStereo", None),
		"RestrictReactionChange": (125, 2, (11, 0), (), "RestrictReactionChange", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"RingBondCount": (118, 2, (3, 0), (), "RingBondCount", None),
		"SBO": (135, 2, (3, 0), (), "SBO", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Stereochemistry": (113, 2, (3, 0), (), "Stereochemistry", None),
		"SubstituentCount": (117, 2, (3, 0), (), "SubstituentCount", None),
		"SubstituentType": (116, 2, (3, 0), (), "SubstituentType", None),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Translation": (121, 2, (3, 0), (), "Translation", None),
		"Unsaturation": (119, 2, (3, 0), (), "Unsaturation", None),
		"UnusedValences": (134, 2, (3, 0), (), "UnusedValences", None),
		"UsedValences": (133, 2, (3, 0), (), "UsedValences", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"AbnormalValenceAllowed": ((124, LCID, 4, 0),()),
		"AtomNumber": ((114, LCID, 4, 0),()),
		"AttachmentPointType": ((140, LCID, 4, 0),()),
		"Charge": ((103, LCID, 4, 0),()),
		"Color": ((5, LCID, 4, 0),()),
		"ElementNumber": ((102, LCID, 4, 0),()),
		"EnhancedStereoGroupNumber": ((143, LCID, 4, 0),()),
		"EnhancedStereoType": ((142, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"ImplicitHydrogensAllowed": ((123, LCID, 4, 0),()),
		"IsAttachmentPoint": ((136, LCID, 4, 0),()),
		"IsHDash": ((112, LCID, 4, 0),()),
		"IsHDot": ((111, LCID, 4, 0),()),
		"IsMultiCenter": ((137, LCID, 4, 0),()),
		"IsVariableAttach": ((138, LCID, 4, 0),()),
		"Isotope": ((105, LCID, 4, 0),()),
		"IsotopicAbundance": ((122, LCID, 4, 0),()),
		"LabelDisplay": ((107, LCID, 4, 0),()),
		"LabelText": ((139, LCID, 4, 0),()),
		"LinkCountHigh": ((127, LCID, 4, 0),()),
		"LinkCountLow": ((126, LCID, 4, 0),()),
		"NumImplicitHydrogens": ((106, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Radical": ((104, LCID, 4, 0),()),
		"ReactionStereo": ((120, LCID, 4, 0),()),
		"RestrictReactionChange": ((125, LCID, 4, 0),()),
		"RingBondCount": ((118, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Stereochemistry": ((113, LCID, 4, 0),()),
		"SubstituentCount": ((117, LCID, 4, 0),()),
		"SubstituentType": ((116, LCID, 4, 0),()),
		"Translation": ((121, LCID, 4, 0),()),
		"Unsaturation": ((119, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawAtoms(DispatchBaseClass):
	'ChemDraw atoms interface'
	CLSID = IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')
	coclass_clsid = IID('{D8276FFA-D137-4E55-9A86-5E73A3407617}')

	# Result is of type IChemDrawAtom
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawBond(DispatchBaseClass):
	'ChemDraw bond interface'
	CLSID = IID('{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')
	coclass_clsid = IID('{5A4404EB-85A0-46D1-9157-97796E11133E}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawAtom
	def OtherAtom(self, thisAtom=defaultNamedNotOptArg):
		"Returns the atom attached to the bond that isn't the specified atom."
		ret = self._oleobj_.InvokeTypes(113, LCID, 1, (9, 0), ((9, 1),),thisAtom
			)
		if ret is not None:
			ret = Dispatch(ret, 'OtherAtom', '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'Atom1' returns object of type 'IChemDrawAtom'
		"Atom1": (101, 2, (9, 0), (), "Atom1", '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}'),
		# Method 'Atom2' returns object of type 'IChemDrawAtom'
		"Atom2": (102, 2, (9, 0), (), "Atom2", '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}'),
		"AttachChar1": (107, 2, (3, 0), (), "AttachChar1", None),
		"AttachChar2": (108, 2, (3, 0), (), "AttachChar2", None),
		"BondDisplay": (104, 2, (3, 0), (), "BondDisplay", None),
		"BondDisplay2": (105, 2, (3, 0), (), "BondDisplay2", None),
		"BondDoublePosition": (106, 2, (3, 0), (), "BondDoublePosition", None),
		"BondOrder": (103, 2, (3, 0), (), "BondOrder", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'CrossingBonds' returns object of type 'IChemDrawBonds'
		"CrossingBonds": (112, 2, (9, 0), (), "CrossingBonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"ReactionParticipation": (110, 2, (3, 0), (), "ReactionParticipation", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Stereochemistry": (111, 2, (3, 0), (), "Stereochemistry", None),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Topology": (109, 2, (3, 0), (), "Topology", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"AttachChar1": ((107, LCID, 4, 0),()),
		"AttachChar2": ((108, LCID, 4, 0),()),
		"BondDisplay": ((104, LCID, 4, 0),()),
		"BondDisplay2": ((105, LCID, 4, 0),()),
		"BondDoublePosition": ((106, LCID, 4, 0),()),
		"BondOrder": ((103, LCID, 4, 0),()),
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"ReactionParticipation": ((110, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Stereochemistry": ((111, LCID, 4, 0),()),
		"Topology": ((109, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawBonds(DispatchBaseClass):
	'ChemDraw bonds interface'
	CLSID = IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')
	coclass_clsid = IID('{ED49B2DA-B782-4C80-B10A-6929EF115652}')

	# Result is of type IChemDrawBond
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawBorder(DispatchBaseClass):
	'ChemDraw border interface'
	CLSID = IID('{40553F42-5954-43F2-B154-188727D588E1}')
	coclass_clsid = IID('{C7B5B8A1-F00F-4DDB-8DB9-C424E3342CF0}')

	_prop_map_get_ = {
		"Color": (3, 2, (19, 0), (), "Color", None),
		"IsDashed": (1, 2, (11, 0), (), "IsDashed", None),
		"Width": (2, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((3, LCID, 4, 0),()),
		"IsDashed": ((1, LCID, 4, 0),()),
		"Width": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawBracket(DispatchBaseClass):
	'ChemDraw bracket object interface'
	CLSID = IID('{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')
	coclass_clsid = IID('{5F717BE1-0415-4397-A493-F61E9315356D}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"BracketLipSize": (107, 2, (3, 0), (), "BracketLipSize", None),
		"BracketType": (103, 2, (3, 0), (), "BracketType", None),
		"BracketUsage": (104, 2, (3, 0), (), "BracketUsage", None),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		"ComponentOrder": (108, 2, (3, 0), (), "ComponentOrder", None),
		# Method 'ContainedAtoms' returns object of type 'IChemDrawAtoms'
		"ContainedAtoms": (114, 2, (9, 0), (), "ContainedAtoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'CrossingBonds' returns object of type 'IChemDrawBonds'
		"CrossingBonds": (111, 2, (9, 0), (), "CrossingBonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'End' returns object of type 'IChemDrawPoint'
		"End": (102, 2, (9, 0), (), "End", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		# Method 'InsideAtoms' returns object of type 'IChemDrawAtoms'
		"InsideAtoms": (112, 2, (9, 0), (), "InsideAtoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		# Method 'OutsideAtoms' returns object of type 'IChemDrawAtoms'
		"OutsideAtoms": (113, 2, (9, 0), (), "OutsideAtoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'PairedBrackets' returns object of type 'IChemDrawBrackets'
		"PairedBrackets": (115, 2, (9, 0), (), "PairedBrackets", '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		"PolymerFlipType": (106, 2, (3, 0), (), "PolymerFlipType", None),
		"PolymerRepeatPattern": (105, 2, (3, 0), (), "PolymerRepeatPattern", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"RepeatCount": (109, 2, (5, 0), (), "RepeatCount", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"SRULabel": (110, 2, (8, 0), (), "SRULabel", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		# Method 'Start' returns object of type 'IChemDrawPoint'
		"Start": (101, 2, (9, 0), (), "Start", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"BracketType": ((103, LCID, 4, 0),()),
		"BracketUsage": ((104, LCID, 4, 0),()),
		"Color": ((5, LCID, 4, 0),()),
		"ComponentOrder": ((108, LCID, 4, 0),()),
		"End": ((102, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"PolymerFlipType": ((106, LCID, 4, 0),()),
		"PolymerRepeatPattern": ((105, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"RepeatCount": ((109, LCID, 4, 0),()),
		"SRULabel": ((110, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Start": ((101, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawBrackets(DispatchBaseClass):
	'ChemDraw bracket objects interface'
	CLSID = IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')
	coclass_clsid = IID('{CC11162C-C954-4859-A9C4-37B6C06C3F4B}')

	# Result is of type IChemDrawBracket
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawCell(DispatchBaseClass):
	'ChemDraw cell interface'
	CLSID = IID('{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}')
	coclass_clsid = IID('{4ABDA8EB-29B0-469D-B937-F213AA330CEC}')

	# Result is of type IChemDrawAltGroup
	def MakeAltGroup(self):
		'Creates a new alternative group in the cell.'
		ret = self._oleobj_.InvokeTypes(409, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeAltGroup', '{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')
		return ret

	# Result is of type IChemDrawArrow
	def MakeArrow(self):
		'Creates a new arrow in the cell.'
		ret = self._oleobj_.InvokeTypes(414, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeArrow', '{669C0868-90B0-4469-9621-7639880698B1}')
		return ret

	# Result is of type IChemDrawAtom
	def MakeAtom(self):
		'Creates a new atom in the cell.'
		ret = self._oleobj_.InvokeTypes(401, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeAtom', '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')
		return ret

	# Result is of type IChemDrawBond
	def MakeBond(self, at1=defaultNamedNotOptArg, at2=defaultNamedNotOptArg):
		'Creates a new bond between two atoms in the cell.'
		ret = self._oleobj_.InvokeTypes(402, LCID, 1, (9, 0), ((9, 1), (9, 1)),at1
			, at2)
		if ret is not None:
			ret = Dispatch(ret, 'MakeBond', '{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')
		return ret

	# Result is of type IChemDrawBracket
	def MakeBracket(self, type=defaultNamedNotOptArg):
		'Creates a new bracket in the cell.'
		ret = self._oleobj_.InvokeTypes(415, LCID, 1, (9, 0), ((3, 1),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeBracket', '{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')
		return ret

	# Result is of type IChemDrawText
	def MakeCaption(self):
		'Creates a new caption in the cell.'
		ret = self._oleobj_.InvokeTypes(405, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeCaption', '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')
		return ret

	# Result is of type IChemDrawConstraint
	def MakeConstraint(self, ConstraintType=defaultNamedNotOptArg):
		'Creates a new constraint in the cell.'
		ret = self._oleobj_.InvokeTypes(411, LCID, 1, (9, 0), ((3, 1),),ConstraintType
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeConstraint', '{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')
		return ret

	# Result is of type IChemDrawGraphic
	def MakeEllipse(self):
		'Creates a new ellipse or circle in the cell.'
		ret = self._oleobj_.InvokeTypes(418, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeEllipse', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	# Result is of type IChemDrawGeometry
	def MakeGeometry(self, geomType=defaultNamedNotOptArg):
		'Creates a new geometry in the cell.'
		ret = self._oleobj_.InvokeTypes(410, LCID, 1, (9, 0), ((3, 1),),geomType
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeGeometry', '{A9173267-C525-4660-93A0-C5FF4BC55057}')
		return ret

	# Result is of type IChemDrawGroup
	def MakeGroup(self):
		'Creates a new group in the cell.'
		ret = self._oleobj_.InvokeTypes(407, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeGroup', '{40957F2E-AC2D-44B4-B237-A7E2A825E636}')
		return ret

	# Result is of type IChemDrawGraphic
	def MakeOrbital(self, type=defaultNamedNotOptArg):
		'Creates a new orbital in the cell.'
		ret = self._oleobj_.InvokeTypes(419, LCID, 1, (9, 0), ((3, 1),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeOrbital', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	# Result is of type IChemDrawPlasmidMap
	def MakePlasmidMap(self):
		'Creates a new plasmid map in the cell.'
		ret = self._oleobj_.InvokeTypes(421, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakePlasmidMap', '{F06B3507-3060-4095-8406-CBBDD00A054E}')
		return ret

	# Result is of type IChemDrawGraphic
	def MakeRectangle(self):
		'Creates a new rectangle in the cell.'
		ret = self._oleobj_.InvokeTypes(417, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeRectangle', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	# Result is of type IChemDrawSpline
	def MakeSpline(self):
		'Creates a new spline in the cell.'
		ret = self._oleobj_.InvokeTypes(404, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeSpline', '{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')
		return ret

	# Result is of type IChemDrawStoichiometryGrid
	def MakeStoichiometryGrid(self):
		'Creates a new stoichiometry grid in the cell.'
		ret = self._oleobj_.InvokeTypes(420, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeStoichiometryGrid', '{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	# Result is of type IChemDrawSymbol
	def MakeSymbol(self, type=defaultNamedNotOptArg):
		'Creates a new symbol in the cell.'
		ret = self._oleobj_.InvokeTypes(416, LCID, 1, (9, 0), ((3, 1),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeSymbol', '{0C9366BF-36BB-4303-86FA-966657FF891D}')
		return ret

	# Result is of type IChemDrawTLCPlate
	def MakeTLCPlate(self):
		'Creates a new TLC plate in the cell.'
		ret = self._oleobj_.InvokeTypes(413, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeTLCPlate', '{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	# Result is of type IChemDrawTable
	def MakeTable(self):
		'Creates a new table in the cell.'
		ret = self._oleobj_.InvokeTypes(408, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeTable', '{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')
		return ret

	_prop_map_get_ = {
		# Method 'AltGroups' returns object of type 'IChemDrawAltGroups'
		"AltGroups": (309, 2, (9, 0), (), "AltGroups", '{D9E5D3D1-0D59-4126-B108-7D567E396FB3}'),
		# Method 'Arrows' returns object of type 'IChemDrawArrows'
		"Arrows": (316, 2, (9, 0), (), "Arrows", '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}'),
		# Method 'Atoms' returns object of type 'IChemDrawAtoms'
		"Atoms": (301, 2, (9, 0), (), "Atoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'Bonds' returns object of type 'IChemDrawBonds'
		"Bonds": (302, 2, (9, 0), (), "Bonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'BottomBorder' returns object of type 'IChemDrawBorder'
		"BottomBorder": (4, 2, (9, 0), (), "BottomBorder", '{40553F42-5954-43F2-B154-188727D588E1}'),
		# Method 'Brackets' returns object of type 'IChemDrawBrackets'
		"Brackets": (320, 2, (9, 0), (), "Brackets", '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}'),
		# Method 'Captions' returns object of type 'IChemDrawTexts'
		"Captions": (305, 2, (9, 0), (), "Captions", '{D156092E-1412-458C-BD6A-3CC171B56E63}'),
		# Method 'Constraints' returns object of type 'IChemDrawConstraints'
		"Constraints": (311, 2, (9, 0), (), "Constraints", '{990C82BE-55F2-49F2-B822-2E448C7FEC80}'),
		# Method 'Geometries' returns object of type 'IChemDrawGeometries'
		"Geometries": (310, 2, (9, 0), (), "Geometries", '{53C77081-53BF-4397-9BB4-84D6AF7C10F3}'),
		# Method 'Graphics' returns object of type 'IChemDrawGraphics'
		"Graphics": (303, 2, (9, 0), (), "Graphics", '{D0E3D4B9-3B16-4331-BBA2-651319AE0402}'),
		# Method 'Groups' returns object of type 'IChemDrawGroups'
		"Groups": (307, 2, (9, 0), (), "Groups", '{E5164832-7AFC-463A-9C19-A1AF6D191020}'),
		# Method 'LeftBorder' returns object of type 'IChemDrawBorder'
		"LeftBorder": (3, 2, (9, 0), (), "LeftBorder", '{40553F42-5954-43F2-B154-188727D588E1}'),
		# Method 'Objects' returns object of type 'IChemDrawObjects'
		"Objects": (1, 2, (9, 0), (), "Objects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		# Method 'Pictures' returns object of type 'IChemDrawPictures'
		"Pictures": (306, 2, (9, 0), (), "Pictures", '{41652842-15D6-44AE-AEFF-B51B179CF019}'),
		# Method 'PlasmidMaps' returns object of type 'IChemDrawPlasmidMaps'
		"PlasmidMaps": (315, 2, (9, 0), (), "PlasmidMaps", '{E06B3507-3060-4095-8406-BAADD00A054E}'),
		# Method 'ReactionSchemes' returns object of type 'IChemDrawReactionSchemes'
		"ReactionSchemes": (312, 2, (9, 0), (), "ReactionSchemes", '{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}'),
		# Method 'RightBorder' returns object of type 'IChemDrawBorder'
		"RightBorder": (5, 2, (9, 0), (), "RightBorder", '{40553F42-5954-43F2-B154-188727D588E1}'),
		# Method 'Splines' returns object of type 'IChemDrawSplines'
		"Splines": (304, 2, (9, 0), (), "Splines", '{272423F1-2909-4340-8870-8062530ADD05}'),
		# Method 'StoichiometryGrids' returns object of type 'IChemDrawStoichiometryGrids'
		"StoichiometryGrids": (314, 2, (9, 0), (), "StoichiometryGrids", '{27109627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Symbols' returns object of type 'IChemDrawSymbols'
		"Symbols": (319, 2, (9, 0), (), "Symbols", '{D44C587D-2434-46B8-8B76-D309A2632456}'),
		# Method 'TLCPlates' returns object of type 'IChemDrawTLCPlates'
		"TLCPlates": (313, 2, (9, 0), (), "TLCPlates", '{27609627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Tables' returns object of type 'IChemDrawTables'
		"Tables": (308, 2, (9, 0), (), "Tables", '{80C78566-D4BF-460E-B055-5728877FB30E}'),
		# Method 'TopBorder' returns object of type 'IChemDrawBorder'
		"TopBorder": (2, 2, (9, 0), (), "TopBorder", '{40553F42-5954-43F2-B154-188727D588E1}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawCells(DispatchBaseClass):
	'ChemDraw cells interface'
	CLSID = IID('{26B98B2C-EE16-49FD-95E5-A8551149C0EF}')
	coclass_clsid = IID('{504B85C3-4DA8-4C83-9C1D-C34C447491C7}')

	# Result is of type IChemDrawCell
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawConstraint(DispatchBaseClass):
	'ChemDraw constraint interface'
	CLSID = IID('{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')
	coclass_clsid = IID('{59D52749-0AE5-4AE5-A5BE-7534DA8DD900}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'BasisObjects' returns object of type 'IChemDrawObjects'
		"BasisObjects": (101, 2, (9, 0), (), "BasisObjects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		"ConstraintType": (102, 2, (3, 0), (), "ConstraintType", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"MaxRange": (104, 2, (5, 0), (), "MaxRange", None),
		"MinRange": (103, 2, (5, 0), (), "MinRange", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"MaxRange": ((104, LCID, 4, 0),()),
		"MinRange": ((103, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawConstraints(DispatchBaseClass):
	'ChemDraw constraints interface'
	CLSID = IID('{990C82BE-55F2-49F2-B822-2E448C7FEC80}')
	coclass_clsid = IID('{A7E7C374-E261-414A-847C-ED92818617F9}')

	# Result is of type IChemDrawConstraint
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawDataType(DispatchBaseClass):
	'IChemDrawDataType Interface'
	CLSID = IID('{BB42A8EF-A444-40C2-BF4F-E156341E4127}')
	coclass_clsid = IID('{1E1AC724-C06D-4078-9E42-DBB291BA236B}')

	_prop_map_get_ = {
		"Extension": (2, 2, (8, 0), (), "Extension", None),
		"MIME": (1, 2, (8, 0), (), "MIME", None),
		"Valid": (3, 2, (11, 0), (), "Valid", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawDataTypes(DispatchBaseClass):
	'IChemDrawDataTypes Interface'
	CLSID = IID('{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}')
	coclass_clsid = IID('{B8DAB55C-E0EC-4337-B1F0-D8ECABD6955F}')

	# Result is of type IChemDrawDataType
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, index=defaultNamedNotOptArg):
		'Returns the data type object at the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{BB42A8EF-A444-40C2-BF4F-E156341E4127}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (2, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Returns the data type object at the given index.'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{BB42A8EF-A444-40C2-BF4F-E156341E4127}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{BB42A8EF-A444-40C2-BF4F-E156341E4127}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawDocument(DispatchBaseClass):
	'IChemDrawDocument interface'
	CLSID = IID('{9E3A4685-0A8F-420D-A73E-4A37B83830DB}')
	coclass_clsid = IID('{41BA6D21-A02E-11CE-8FD9-0020AFD1F20C}')

	def Activate(self):
		'Activate this document'
		return self._oleobj_.InvokeTypes(1610743820, LCID, 1, (24, 0), (),)

	def Close(self, saveChanges=defaultNamedOptArg, Filename=defaultNamedOptArg):
		'Close this document.'
		return self._oleobj_.InvokeTypes(1610743821, LCID, 1, (24, 0), ((16396, 17), (16396, 17)),saveChanges
			, Filename)

	# Result is of type IChemDrawAltGroup
	def MakeAltGroup(self):
		'Creates a new alternative group in the document.'
		ret = self._oleobj_.InvokeTypes(409, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeAltGroup', '{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')
		return ret

	# Result is of type IChemDrawArrow
	def MakeArrow(self):
		'Creates a new arrow in the document.'
		ret = self._oleobj_.InvokeTypes(414, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeArrow', '{669C0868-90B0-4469-9621-7639880698B1}')
		return ret

	# Result is of type IChemDrawAtom
	def MakeAtom(self):
		'Creates a new atom in the document.'
		ret = self._oleobj_.InvokeTypes(401, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeAtom', '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')
		return ret

	# Result is of type IChemDrawBond
	def MakeBond(self, at1=defaultNamedNotOptArg, at2=defaultNamedNotOptArg):
		'Creates a new bond between two atoms in the document.'
		ret = self._oleobj_.InvokeTypes(402, LCID, 1, (9, 0), ((9, 1), (9, 1)),at1
			, at2)
		if ret is not None:
			ret = Dispatch(ret, 'MakeBond', '{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')
		return ret

	# Result is of type IChemDrawBracket
	def MakeBracket(self, type=defaultNamedNotOptArg):
		'Creates a new bracket in the document.'
		ret = self._oleobj_.InvokeTypes(415, LCID, 1, (9, 0), ((3, 1),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeBracket', '{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')
		return ret

	# Result is of type IChemDrawText
	def MakeCaption(self):
		'Creates a new caption in the document.'
		ret = self._oleobj_.InvokeTypes(405, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeCaption', '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')
		return ret

	# Result is of type IChemDrawConstraint
	def MakeConstraint(self, ConstraintType=defaultNamedNotOptArg):
		'Creates a new constraint in the document.'
		ret = self._oleobj_.InvokeTypes(411, LCID, 1, (9, 0), ((3, 1),),ConstraintType
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeConstraint', '{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')
		return ret

	# Result is of type IChemDrawGraphic
	def MakeEllipse(self):
		'Creates a new ellipse or circle in the document.'
		ret = self._oleobj_.InvokeTypes(418, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeEllipse', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	# Result is of type IChemDrawGeometry
	def MakeGeometry(self, geomType=defaultNamedNotOptArg):
		'Creates a new geometry in the document.'
		ret = self._oleobj_.InvokeTypes(410, LCID, 1, (9, 0), ((3, 1),),geomType
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeGeometry', '{A9173267-C525-4660-93A0-C5FF4BC55057}')
		return ret

	# Result is of type IChemDrawGroup
	def MakeGroup(self):
		'Creates a new group in the document.'
		ret = self._oleobj_.InvokeTypes(407, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeGroup', '{40957F2E-AC2D-44B4-B237-A7E2A825E636}')
		return ret

	# Result is of type IChemDrawGraphic
	def MakeOrbital(self, type=defaultNamedNotOptArg):
		'Creates a new orbital in the document.'
		ret = self._oleobj_.InvokeTypes(419, LCID, 1, (9, 0), ((3, 1),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeOrbital', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	# Result is of type IChemDrawPlasmidMap
	def MakePlasmidMap(self):
		'Creates a new plasmid map in the document.'
		ret = self._oleobj_.InvokeTypes(421, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakePlasmidMap', '{F06B3507-3060-4095-8406-CBBDD00A054E}')
		return ret

	# Result is of type IChemDrawGraphic
	def MakeRectangle(self):
		'Creates a new rectangle in the document.'
		ret = self._oleobj_.InvokeTypes(417, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeRectangle', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	# Result is of type IChemDrawSpline
	def MakeSpline(self):
		'Creates a new spline in the document.'
		ret = self._oleobj_.InvokeTypes(404, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeSpline', '{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')
		return ret

	# Result is of type IChemDrawStoichiometryGrid
	def MakeStoichiometryGrid(self):
		'Creates a new stoichiometry grid in the document.'
		ret = self._oleobj_.InvokeTypes(420, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeStoichiometryGrid', '{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	# Result is of type IChemDrawSymbol
	def MakeSymbol(self, type=defaultNamedNotOptArg):
		'Creates a new symbol in the document.'
		ret = self._oleobj_.InvokeTypes(416, LCID, 1, (9, 0), ((3, 1),),type
			)
		if ret is not None:
			ret = Dispatch(ret, 'MakeSymbol', '{0C9366BF-36BB-4303-86FA-966657FF891D}')
		return ret

	# Result is of type IChemDrawTLCPlate
	def MakeTLCPlate(self):
		'Creates a new TLC plate in the document.'
		ret = self._oleobj_.InvokeTypes(413, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeTLCPlate', '{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	# Result is of type IChemDrawTable
	def MakeTable(self):
		'Creates a new table in the document.'
		ret = self._oleobj_.InvokeTypes(408, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'MakeTable', '{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')
		return ret

	def Paste(self):
		'Add the contents of the clipboard to the document.'
		return self._oleobj_.InvokeTypes(1610743828, LCID, 1, (24, 0), (),)

	def Print(self, From=defaultNamedOptArg, to=defaultNamedOptArg, copies=defaultNamedOptArg):
		'Print this document.'
		return self._oleobj_.InvokeTypes(1610743822, LCID, 1, (24, 0), ((16396, 17), (16396, 17), (16396, 17)),From
			, to, copies)

	def PrintOut(self, From=defaultNamedOptArg, to=defaultNamedOptArg, copies=defaultNamedOptArg):
		'Print this document.'
		return self._oleobj_.InvokeTypes(1610743829, LCID, 1, (24, 0), ((16396, 17), (16396, 17), (16396, 17)),From
			, to, copies)

	def Redo(self):
		'Restore the last change to a file that was recently undone.'
		return self._oleobj_.InvokeTypes(1610743826, LCID, 1, (24, 0), (),)

	def Save(self):
		'Saves changes to the file specified in the FullName property.'
		return self._oleobj_.InvokeTypes(1610743823, LCID, 1, (24, 0), (),)

	def SaveAs(self, Filename=defaultNamedOptArg, Format=defaultNamedOptArg, resolution=defaultNamedOptArg, Width=defaultNamedOptArg
			, Height=defaultNamedOptArg):
		'Saves changes to a file.'
		return self._oleobj_.InvokeTypes(1610743824, LCID, 1, (24, 0), ((16396, 17), (16396, 17), (16396, 17), (16396, 17), (16396, 17)),Filename
			, Format, resolution, Width, Height)

	def Undo(self):
		'Undo the last change made to a file.'
		return self._oleobj_.InvokeTypes(1610743825, LCID, 1, (24, 0), (),)

	def Zoom(self, factor=defaultNamedNotOptArg, Center=0):
		'Modify the magnification level of the document, as a percentage.'
		return self._oleobj_.InvokeTypes(1610743832, LCID, 1, (24, 0), ((5, 1), (9, 49)),factor
			, Center)

	def ZoomIn(self, Center=0):
		"Increment the document's magnification level."
		return self._oleobj_.InvokeTypes(1610743830, LCID, 1, (24, 0), ((9, 49),),Center
			)

	def ZoomOut(self, Center=0):
		"Decrement the document's magnification level."
		return self._oleobj_.InvokeTypes(1610743831, LCID, 1, (24, 0), ((9, 49),),Center
			)

	_prop_map_get_ = {
		# Method 'AltGroups' returns object of type 'IChemDrawAltGroups'
		"AltGroups": (309, 2, (9, 0), (), "AltGroups", '{D9E5D3D1-0D59-4126-B108-7D567E396FB3}'),
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (27, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		# Method 'Application' returns object of type 'IChemDrawApplication'
		"Application": (2, 2, (9, 0), (), "Application", '{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}'),
		# Method 'Arrows' returns object of type 'IChemDrawArrows'
		"Arrows": (316, 2, (9, 0), (), "Arrows", '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}'),
		# Method 'Atoms' returns object of type 'IChemDrawAtoms'
		"Atoms": (301, 2, (9, 0), (), "Atoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'Bonds' returns object of type 'IChemDrawBonds'
		"Bonds": (302, 2, (9, 0), (), "Bonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'Brackets' returns object of type 'IChemDrawBrackets'
		"Brackets": (320, 2, (9, 0), (), "Brackets", '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}'),
		# Method 'CaptionBeingEdited' returns object of type 'IChemDrawText'
		"CaptionBeingEdited": (17, 2, (9, 0), (), "CaptionBeingEdited", '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}'),
		# Method 'Captions' returns object of type 'IChemDrawTexts'
		"Captions": (305, 2, (9, 0), (), "Captions", '{D156092E-1412-458C-BD6A-3CC171B56E63}'),
		# Method 'Constraints' returns object of type 'IChemDrawConstraints'
		"Constraints": (311, 2, (9, 0), (), "Constraints", '{990C82BE-55F2-49F2-B822-2E448C7FEC80}'),
		# Method 'DataObject' returns object of type 'DataObject'
		"DataObject": (8, 2, (9, 0), (), "DataObject", '{41A7D760-6018-11CF-9016-00AA0068841E}'),
		"DrawingSpace": (18, 2, (3, 0), (), "DrawingSpace", None),
		"FullName": (3, 2, (8, 0), (), "FullName", None),
		# Method 'Geometries' returns object of type 'IChemDrawGeometries'
		"Geometries": (310, 2, (9, 0), (), "Geometries", '{53C77081-53BF-4397-9BB4-84D6AF7C10F3}'),
		# Method 'Graphics' returns object of type 'IChemDrawGraphics'
		"Graphics": (303, 2, (9, 0), (), "Graphics", '{D0E3D4B9-3B16-4331-BBA2-651319AE0402}'),
		# Method 'Groups' returns object of type 'IChemDrawGroups'
		"Groups": (307, 2, (9, 0), (), "Groups", '{E5164832-7AFC-463A-9C19-A1AF6D191020}'),
		"Height": (19, 2, (5, 0), (), "Height", None),
		"Magnification": (26, 2, (5, 0), (), "Magnification", None),
		"Modified": (14, 2, (11, 0), (), "Modified", None),
		"NumChemicalWarnings": (25, 2, (3, 0), (), "NumChemicalWarnings", None),
		"NumPagesHigh": (21, 2, (3, 0), (), "NumPagesHigh", None),
		"NumPagesWide": (22, 2, (3, 0), (), "NumPagesWide", None),
		# Method 'Objects' returns object of type 'IChemDrawObjects'
		"Objects": (9, 2, (9, 0), (), "Objects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		"Overlap": (23, 2, (5, 0), (), "Overlap", None),
		# Method 'Parent' returns object of type 'IChemDrawDocuments'
		"Parent": (4, 2, (9, 0), (), "Parent", '{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}'),
		"Path": (5, 2, (8, 0), (), "Path", None),
		# Method 'Pictures' returns object of type 'IChemDrawPictures'
		"Pictures": (306, 2, (9, 0), (), "Pictures", '{41652842-15D6-44AE-AEFF-B51B179CF019}'),
		# Method 'PlasmidMaps' returns object of type 'IChemDrawPlasmidMaps'
		"PlasmidMaps": (315, 2, (9, 0), (), "PlasmidMaps", '{E06B3507-3060-4095-8406-BAADD00A054E}'),
		"PrintRegMarks": (24, 2, (11, 0), (), "PrintRegMarks", None),
		# Method 'ReactionSchemes' returns object of type 'IChemDrawReactionSchemes'
		"ReactionSchemes": (312, 2, (9, 0), (), "ReactionSchemes", '{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}'),
		"ReadOnly": (6, 2, (11, 0), (), "ReadOnly", None),
		"Saved": (7, 2, (11, 0), (), "Saved", None),
		# Method 'Selection' returns object of type 'IChemDrawSelection'
		"Selection": (10, 2, (9, 0), (), "Selection", '{2590DD54-2A58-4A2A-AF35-5EE4CE3EABFA}'),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (11, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"ShowCrosshair": (15, 2, (11, 0), (), "ShowCrosshair", None),
		"ShowRulers": (16, 2, (11, 0), (), "ShowRulers", None),
		# Method 'Splines' returns object of type 'IChemDrawSplines'
		"Splines": (304, 2, (9, 0), (), "Splines", '{272423F1-2909-4340-8870-8062530ADD05}'),
		# Method 'StoichiometryGrids' returns object of type 'IChemDrawStoichiometryGrids'
		"StoichiometryGrids": (314, 2, (9, 0), (), "StoichiometryGrids", '{27109627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Symbols' returns object of type 'IChemDrawSymbols'
		"Symbols": (319, 2, (9, 0), (), "Symbols", '{D44C587D-2434-46B8-8B76-D309A2632456}'),
		# Method 'TLCPlates' returns object of type 'IChemDrawTLCPlates'
		"TLCPlates": (313, 2, (9, 0), (), "TLCPlates", '{27609627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Tables' returns object of type 'IChemDrawTables'
		"Tables": (308, 2, (9, 0), (), "Tables", '{80C78566-D4BF-460E-B055-5728877FB30E}'),
		"Width": (20, 2, (5, 0), (), "Width", None),
		"name": (1, 2, (8, 0), (), "name", None),
	}
	_prop_map_put_ = {
		"CaptionBeingEdited": ((17, LCID, 4, 0),()),
		"DrawingSpace": ((18, LCID, 4, 0),()),
		"Height": ((19, LCID, 4, 0),()),
		"Magnification": ((26, LCID, 4, 0),()),
		"Modified": ((14, LCID, 4, 0),()),
		"NumPagesHigh": ((21, LCID, 4, 0),()),
		"NumPagesWide": ((22, LCID, 4, 0),()),
		"Overlap": ((23, LCID, 4, 0),()),
		"PrintRegMarks": ((24, LCID, 4, 0),()),
		"ShowCrosshair": ((15, LCID, 4, 0),()),
		"ShowRulers": ((16, LCID, 4, 0),()),
		"Width": ((20, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawDocuments(DispatchBaseClass):
	'IChemDrawDocuments interface'
	CLSID = IID('{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}')
	coclass_clsid = IID('{EFD13774-5475-4FE1-A9BC-32FACFC0FEF2}')

	# Result is of type IChemDrawDocument
	def Add(self):
		'Create a new document'
		ret = self._oleobj_.InvokeTypes(1610743813, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{9E3A4685-0A8F-420D-A73E-4A37B83830DB}')
		return ret

	def Close(self):
		'Close all the documents in the collection'
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (24, 0), (),)

	def Item(self, index=defaultNamedOptArg):
		'Given an index, returns a document in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 17),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	# Result is of type IChemDrawDocument
	def Open(self, Filename=defaultNamedNotOptArg, password=defaultNamedOptArg, Format=defaultNamedOptArg):
		'Open an existing document'
		ret = self._oleobj_.InvokeTypes(1610743815, LCID, 1, (9, 0), ((8, 1), (16396, 17), (16396, 17)),Filename
			, password, Format)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{9E3A4685-0A8F-420D-A73E-4A37B83830DB}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type 'IChemDrawApplication'
		"Application": (1, 2, (9, 0), (), "Application", '{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}'),
		"Count": (2, 2, (3, 0), (), "Count", None),
		# Method 'Parent' returns object of type 'IChemDrawApplication'
		"Parent": (3, 2, (9, 0), (), "Parent", '{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}'),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedOptArg):
		'Given an index, returns a document in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 17),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawFragmentationAnalyzer(DispatchBaseClass):
	'ChemDraw fragmentation event interface'
	CLSID = IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2AAA}')
	coclass_clsid = IID('{D716300D-8CBF-40FF-9C58-9CCEA0F34DDD}')

	def HighlightNone(self):
		'Unhighlight all the fragments.'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def SelectAll(self):
		'Select all the fragments.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	def SelectNone(self):
		'Unselect all the fragments.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def Update(self):
		'Update the analysis.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AutoUpdate": (11, 2, (11, 0), (), "AutoUpdate", None),
		# Method 'CurrentFragment' returns object of type 'IChemDrawMassFragment'
		"CurrentFragment": (6, 2, (9, 0), (), "CurrentFragment", '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}'),
		"CurrentFragmentID": (12, 2, (3, 0), (), "CurrentFragmentID", None),
		"FragmentationAnalyzerType": (4, 2, (3, 0), (), "FragmentationAnalyzerType", None),
		# Method 'FragmentationLines' returns object of type 'IChemDrawFragmentationLines'
		"FragmentationLines": (3, 2, (9, 0), (), "FragmentationLines", '{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}'),
		# Method 'MassFragments' returns object of type 'IChemDrawMassFragments'
		"MassFragments": (2, 2, (9, 0), (), "MassFragments", '{F745F388-8D27-4BE8-9A3E-A082E20EECCC}'),
		# Method 'Owner' returns object of type 'IChemDrawGroup'
		"Owner": (5, 2, (9, 0), (), "Owner", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
	}
	_prop_map_put_ = {
		"AutoUpdate": ((11, LCID, 4, 0),()),
		"FragmentationAnalyzerType": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawFragmentationLine(DispatchBaseClass):
	'ChemDraw fragmentation line interface'
	CLSID = IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}')
	coclass_clsid = IID('{D716300D-8CBF-40FF-9C58-9CCEA0F3EFFF}')

	_prop_map_get_ = {
		# Method 'CrossedBonds' returns object of type 'IChemDrawBonds'
		"CrossedBonds": (2, 2, (9, 0), (), "CrossedBonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'Spline' returns object of type 'IChemDrawSpline'
		"Spline": (1, 2, (9, 0), (), "Spline", '{380714EE-CEC4-43C7-9D98-1CA296E19AD3}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawFragmentationLines(DispatchBaseClass):
	'ChemDraw fragmentation lines interface'
	CLSID = IID('{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}')
	coclass_clsid = IID('{7D717A46-968E-47EB-B78E-C32DD437EFFF}')

	# Result is of type IChemDrawFragmentationLine
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawGeometries(DispatchBaseClass):
	'ChemDraw geometries interface'
	CLSID = IID('{53C77081-53BF-4397-9BB4-84D6AF7C10F3}')
	coclass_clsid = IID('{3DA3006C-EA2E-4E6C-A9C0-163A5774A3EF}')

	# Result is of type IChemDrawGeometry
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A9173267-C525-4660-93A0-C5FF4BC55057}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A9173267-C525-4660-93A0-C5FF4BC55057}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A9173267-C525-4660-93A0-C5FF4BC55057}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawGeometry(DispatchBaseClass):
	'ChemDraw geometry interface'
	CLSID = IID('{A9173267-C525-4660-93A0-C5FF4BC55057}')
	coclass_clsid = IID('{425C0C02-0AC8-48F4-A0F7-E6E7A61EDB2A}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'BasisObjects' returns object of type 'IChemDrawObjects'
		"BasisObjects": (101, 2, (9, 0), (), "BasisObjects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"GeometryType": (102, 2, (3, 0), (), "GeometryType", None),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"RelationValue": (103, 2, (5, 0), (), "RelationValue", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"RelationValue": ((103, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawGraphic(DispatchBaseClass):
	'ChemDraw graphic object interface'
	CLSID = IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')
	coclass_clsid = IID('{637AB4EC-B34C-4708-B06A-E8E5922302AA}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'DelocalizedBonds' returns object of type 'IChemDrawBonds'
		"DelocalizedBonds": (118, 2, (9, 0), (), "DelocalizedBonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"GraphicType": (103, 2, (3, 0), (), "GraphicType", None),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"IsBold": (113, 2, (11, 0), (), "IsBold", None),
		"IsCircle": (108, 2, (11, 0), (), "IsCircle", None),
		"IsDashed": (114, 2, (11, 0), (), "IsDashed", None),
		"IsFilled": (115, 2, (11, 0), (), "IsFilled", None),
		"IsOrbital": (110, 2, (11, 0), (), "IsOrbital", None),
		"IsOval": (109, 2, (11, 0), (), "IsOval", None),
		"IsRectangle": (111, 2, (11, 0), (), "IsRectangle", None),
		"IsRoundedRectangle": (112, 2, (11, 0), (), "IsRoundedRectangle", None),
		"IsShaded": (116, 2, (11, 0), (), "IsShaded", None),
		"IsShadowed": (117, 2, (11, 0), (), "IsShadowed", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"LineType": (104, 2, (3, 0), (), "LineType", None),
		# Method 'MajorAxisEnd' returns object of type 'IChemDrawPoint'
		"MajorAxisEnd": (101, 2, (9, 0), (), "MajorAxisEnd", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'MinorAxisEnd' returns object of type 'IChemDrawPoint'
		"MinorAxisEnd": (102, 2, (9, 0), (), "MinorAxisEnd", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"OrbitalType": (107, 2, (3, 0), (), "OrbitalType", None),
		"OvalType": (106, 2, (3, 0), (), "OvalType", None),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"RectangleType": (105, 2, (3, 0), (), "RectangleType", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"IsBold": ((113, LCID, 4, 0),()),
		"IsDashed": ((114, LCID, 4, 0),()),
		"IsFilled": ((115, LCID, 4, 0),()),
		"IsShaded": ((116, LCID, 4, 0),()),
		"MajorAxisEnd": ((101, LCID, 4, 0),()),
		"MinorAxisEnd": ((102, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawGraphics(DispatchBaseClass):
	'ChemDraw graphic objects interface'
	CLSID = IID('{D0E3D4B9-3B16-4331-BBA2-651319AE0402}')
	coclass_clsid = IID('{05B8BA9A-2869-44AD-A3FB-A8D6F392F6FC}')

	# Result is of type IChemDrawGraphic
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{24399466-10ED-4161-B216-1C57E5CE4F50}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{24399466-10ED-4161-B216-1C57E5CE4F50}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawGroup(DispatchBaseClass):
	'ChemDraw group interface'
	CLSID = IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')
	coclass_clsid = IID('{1C41DA07-5244-447F-AD57-43DCD32F88A5}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawFragmentationAnalyzer
	# The method FragmentationAnalyzer is actually a property, but must be used as a method to correctly pass the arguments
	def FragmentationAnalyzer(self, pVal=defaultNamedNotOptArg):
		'Returns the fragmentation event of this group.'
		ret = self._oleobj_.InvokeTypes(322, LCID, 2, (9, 0), ((9, 1),),pVal
			)
		if ret is not None:
			ret = Dispatch(ret, 'FragmentationAnalyzer', '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2AAA}')
		return ret

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'AltGroups' returns object of type 'IChemDrawAltGroups'
		"AltGroups": (309, 2, (9, 0), (), "AltGroups", '{D9E5D3D1-0D59-4126-B108-7D567E396FB3}'),
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'Arrows' returns object of type 'IChemDrawArrows'
		"Arrows": (316, 2, (9, 0), (), "Arrows", '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}'),
		# Method 'Atoms' returns object of type 'IChemDrawAtoms'
		"Atoms": (301, 2, (9, 0), (), "Atoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'Bonds' returns object of type 'IChemDrawBonds'
		"Bonds": (302, 2, (9, 0), (), "Bonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		# Method 'Brackets' returns object of type 'IChemDrawBrackets'
		"Brackets": (320, 2, (9, 0), (), "Brackets", '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}'),
		# Method 'Captions' returns object of type 'IChemDrawTexts'
		"Captions": (305, 2, (9, 0), (), "Captions", '{D156092E-1412-458C-BD6A-3CC171B56E63}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Constraints' returns object of type 'IChemDrawConstraints'
		"Constraints": (311, 2, (9, 0), (), "Constraints", '{990C82BE-55F2-49F2-B822-2E448C7FEC80}'),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Geometries' returns object of type 'IChemDrawGeometries'
		"Geometries": (310, 2, (9, 0), (), "Geometries", '{53C77081-53BF-4397-9BB4-84D6AF7C10F3}'),
		# Method 'Graphics' returns object of type 'IChemDrawGraphics'
		"Graphics": (303, 2, (9, 0), (), "Graphics", '{D0E3D4B9-3B16-4331-BBA2-651319AE0402}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"GroupType": (102, 2, (3, 0), (), "GroupType", None),
		# Method 'Groups' returns object of type 'IChemDrawGroups'
		"Groups": (307, 2, (9, 0), (), "Groups", '{E5164832-7AFC-463A-9C19-A1AF6D191020}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Integral": (103, 2, (11, 0), (), "Integral", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		# Method 'Objects' returns object of type 'IChemDrawObjects'
		"Objects": (101, 2, (9, 0), (), "Objects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Pictures' returns object of type 'IChemDrawPictures'
		"Pictures": (306, 2, (9, 0), (), "Pictures", '{41652842-15D6-44AE-AEFF-B51B179CF019}'),
		# Method 'PlasmidMaps' returns object of type 'IChemDrawPlasmidMaps'
		"PlasmidMaps": (315, 2, (9, 0), (), "PlasmidMaps", '{E06B3507-3060-4095-8406-BAADD00A054E}'),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'ReactionSchemes' returns object of type 'IChemDrawReactionSchemes'
		"ReactionSchemes": (312, 2, (9, 0), (), "ReactionSchemes", '{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		"SequenceType": (104, 2, (3, 0), (), "SequenceType", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		# Method 'Splines' returns object of type 'IChemDrawSplines'
		"Splines": (304, 2, (9, 0), (), "Splines", '{272423F1-2909-4340-8870-8062530ADD05}'),
		# Method 'StoichiometryGrids' returns object of type 'IChemDrawStoichiometryGrids'
		"StoichiometryGrids": (314, 2, (9, 0), (), "StoichiometryGrids", '{27109627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Symbols' returns object of type 'IChemDrawSymbols'
		"Symbols": (319, 2, (9, 0), (), "Symbols", '{D44C587D-2434-46B8-8B76-D309A2632456}'),
		# Method 'TLCPlates' returns object of type 'IChemDrawTLCPlates'
		"TLCPlates": (313, 2, (9, 0), (), "TLCPlates", '{27609627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Tables' returns object of type 'IChemDrawTables'
		"Tables": (308, 2, (9, 0), (), "Tables", '{80C78566-D4BF-460E-B055-5728877FB30E}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Integral": ((103, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"SequenceType": ((104, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawGroups(DispatchBaseClass):
	'ChemDraw groups interface'
	CLSID = IID('{E5164832-7AFC-463A-9C19-A1AF6D191020}')
	coclass_clsid = IID('{47CF6326-FBAF-49C9-BA9C-F6242EB52DC6}')

	# Result is of type IChemDrawGroup
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{40957F2E-AC2D-44B4-B237-A7E2A825E636}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{40957F2E-AC2D-44B4-B237-A7E2A825E636}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{40957F2E-AC2D-44B4-B237-A7E2A825E636}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawMassFragment(DispatchBaseClass):
	'ChemDraw mass fragment interface'
	CLSID = IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}')
	coclass_clsid = IID('{D716300D-8CBF-40FF-9C58-9CCEA0F34FFF}')

	_prop_map_get_ = {
		# Method 'BrokenBonds' returns object of type 'IChemDrawBonds'
		"BrokenBonds": (4, 2, (9, 0), (), "BrokenBonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'FragmentationLines' returns object of type 'IChemDrawFragmentationLines'
		"FragmentationLines": (3, 2, (9, 0), (), "FragmentationLines", '{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}'),
		"Highlighted": (5, 2, (11, 0), (), "Highlighted", None),
		"ID": (1, 2, (3, 0), (), "ID", None),
		# Method 'Objects' returns object of type 'IChemDrawObjects'
		"Objects": (2, 2, (9, 0), (), "Objects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
	}
	_prop_map_put_ = {
		"Highlighted": ((5, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawMassFragments(DispatchBaseClass):
	'ChemDraw mass fragments interface'
	CLSID = IID('{F745F388-8D27-4BE8-9A3E-A082E20EECCC}')
	coclass_clsid = IID('{7D717A46-968E-47EB-B78E-C32DD437DFFF}')

	# Result is of type IChemDrawMassFragment
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawObject(DispatchBaseClass):
	'ChemDraw object interface'
	CLSID = IID('{A341E650-F6F0-4068-B499-C231DDEBFBFD}')
	coclass_clsid = IID('{D716300D-8CBF-40FF-9C58-9CCEA0F3EFFF}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawObjectTag(DispatchBaseClass):
	'ChemDraw object tag interface'
	CLSID = IID('{6DA748D4-4F21-45EA-BF09-F493643180F0}')
	coclass_clsid = IID('{DA5D0F99-162A-45B0-B81B-0F48A4781DE2}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		"DoubleValue": (103, 2, (5, 0), (), "DoubleValue", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"LongValue": (104, 2, (3, 0), (), "LongValue", None),
		"ObjectTagType": (102, 2, (3, 0), (), "ObjectTagType", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		# Method 'Owner' returns object of type 'IChemDrawObject'
		"Owner": (106, 2, (9, 0), (), "Owner", '{A341E650-F6F0-4068-B499-C231DDEBFBFD}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		"Persistent": (111, 2, (11, 0), (), "Persistent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"PositioningAngle": (108, 2, (5, 0), (), "PositioningAngle", None),
		# Method 'PositioningOffset' returns object of type 'IChemDrawPoint'
		"PositioningOffset": (109, 2, (9, 0), (), "PositioningOffset", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"PositioningType": (107, 2, (3, 0), (), "PositioningType", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"StringValue": (105, 2, (8, 0), (), "StringValue", None),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Tracking": (110, 2, (11, 0), (), "Tracking", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		# Method 'caption' returns object of type 'IChemDrawText'
		"caption": (101, 2, (9, 0), (), "caption", '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}'),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"DoubleValue": ((103, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"LongValue": ((104, LCID, 4, 0),()),
		"Owner": ((106, LCID, 4, 0),()),
		"Persistent": ((111, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"PositioningAngle": ((108, LCID, 4, 0),()),
		"PositioningOffset": ((109, LCID, 4, 0),()),
		"PositioningType": ((107, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"StringValue": ((105, LCID, 4, 0),()),
		"Tracking": ((110, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawObjectTags(DispatchBaseClass):
	'ChemDraw object tags interface'
	CLSID = IID('{05BE5E8B-5983-46E5-81A8-F80F5C21957A}')
	coclass_clsid = IID('{F5F5A846-177D-4987-8D57-B3A401618C04}')

	# Result is of type IChemDrawObjectTag
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawObjects(DispatchBaseClass):
	'ChemDraw objects interface'
	CLSID = IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')
	coclass_clsid = IID('{75DC8A59-DF79-481D-82F6-0BA538978791}')

	def Add(self, pVal=defaultNamedNotOptArg):
		'Add an object to the collection.  Caution: may fail for some types of collections.'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (24, 0), ((9, 1),),pVal
			)

	def Clean(self, deNovo=False):
		'Tidy the visual represention of a structure.'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((11, 49),),deNovo
			)

	def Clear(self):
		'Clears the objects from the parent.'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def ClearReactionMap(self):
		'Clears the reaction mapping.'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjects
	def Clone(self):
		'Returns a copy of this collection that can then be modified.'
		ret = self._oleobj_.InvokeTypes(45, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Clone', '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')
		return ret

	def Contains(self, pVal=defaultNamedNotOptArg):
		'Returns whether an object is fully contained within this object.'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (11, 0), ((9, 1),),pVal
			)

	def ContractObjectsToLabel(self, bstrLabel=defaultNamedNotOptArg):
		'Contract the objects into a single atom label.'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), ((8, 1),),bstrLabel
			)

	def Copy(self):
		'Copy the objects to the clipboard.'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Copy the objects to the clipboard and remove them from the document.'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), (),)

	def ExpandLabelsToStructure(self):
		'Expand all labels to explicitly show the structure.'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), (),)

	def FilterByTag(self, tagName=defaultNamedNotOptArg, includeThese=defaultNamedNotOptArg, pVal=pythoncom.Missing):
		'Return the collection of these objects that have an Object Tag of the specified name.'
		return self._ApplyTypes_(28, 1, (24, 0), ((8, 1), (11, 1), (16393, 2)), 'FilterByTag', None,tagName
			, includeThese, pVal)

	def FilterByTagDouble(self, tagName=defaultNamedNotOptArg, tagValue=defaultNamedNotOptArg, includeThese=defaultNamedNotOptArg, pVal=pythoncom.Missing):
		'Return the collection of these objects that have an Object Tag of the specified name and value.'
		return self._ApplyTypes_(29, 1, (24, 0), ((8, 1), (5, 1), (11, 1), (16393, 2)), 'FilterByTagDouble', None,tagName
			, tagValue, includeThese, pVal)

	def FilterByTagLong(self, tagName=defaultNamedNotOptArg, tagValue=defaultNamedNotOptArg, includeThese=defaultNamedNotOptArg, pVal=pythoncom.Missing):
		'Return the collection of these objects that have an Object Tag of the specified name and value.'
		return self._ApplyTypes_(30, 1, (24, 0), ((8, 1), (3, 1), (11, 1), (16393, 2)), 'FilterByTagLong', None,tagName
			, tagValue, includeThese, pVal)

	def FilterByTagString(self, tagName=defaultNamedNotOptArg, tagValue=defaultNamedNotOptArg, includeThese=defaultNamedNotOptArg, pVal=pythoncom.Missing):
		'Return the collection of these objects that have an Object Tag of the specified name and value.'
		return self._ApplyTypes_(31, 1, (24, 0), ((8, 1), (8, 1), (11, 1), (16393, 2)), 'FilterByTagString', None,tagName
			, tagValue, includeThese, pVal)

	def Flip(self, vertical=False, preservingAbsoluteStereochemistry=False):
		'Flip these objects horizontally or vertically.'
		return self._oleobj_.InvokeTypes(26, LCID, 1, (24, 0), ((11, 49), (11, 49)),vertical
			, preservingAbsoluteStereochemistry)

	# The method GetData is actually a property, but must be used as a method to correctly pass the arguments
	def GetData(self, dataType=defaultNamedOptArg, resolution=defaultNamedOptArg, Width=defaultNamedOptArg, Height=defaultNamedOptArg):
		'Returns the data of the objects.'
		return self._ApplyTypes_(21, 2, (12, 0), ((12, 17), (12, 17), (12, 17), (12, 17)), 'GetData', None,dataType
			, resolution, Width, Height)

	# Result is of type IChemDrawObject
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A341E650-F6F0-4068-B499-C231DDEBFBFD}')
		return ret

	def Join(self, pVal=defaultNamedNotOptArg):
		'Join these objects with some other objects.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((9, 1),),pVal
			)

	def MakeAttachedData(self, name=defaultNamedNotOptArg, newText=defaultNamedNotOptArg):
		'Creates a data object attached to the objects.'
		return self._oleobj_.InvokeTypes(40, LCID, 1, (24, 0), ((8, 1), (16393, 1)),name
			, newText)

	def MapReactionAtoms(self):
		'Maps the reaction atoms.'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def Move(self, dx=0.0, dy=0.0):
		'Offset the objects by the specified amount, in points.'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((5, 49), (5, 49)),dx
			, dy)

	def Remove(self, pVal=defaultNamedNotOptArg):
		'Remove an object from the collection.  Caution: may fail for some types of collections.'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (24, 0), ((9, 1),),pVal
			)

	def Rotate(self, degrees=defaultNamedNotOptArg, rotateLabels=False):
		'Rotate the objects by the specified angle (labels can be rotated with objects).'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), ((5, 1), (11, 49)),degrees
			, rotateLabels)

	def Scale(self, factor=defaultNamedNotOptArg, scaleLabels=True, scaleSettings=True):
		'Scale the objects by a specified factor.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((5, 1), (11, 49), (11, 49)),factor
			, scaleLabels, scaleSettings)

	def ScaleXYZ(self, factorX=defaultNamedNotOptArg, factorY=defaultNamedNotOptArg, factorZ=1.0, scaleLabels=True
			, scaleSettings=True):
		'Scale the objects by a specified factor.'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 49), (11, 49), (11, 49)),factorX
			, factorY, factorZ, scaleLabels, scaleSettings)

	def Select(self):
		'Selects the objects in the parent.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), (),)

	# The method SetData is actually a property, but must be used as a method to correctly pass the arguments
	def SetData(self, dataType=defaultNamedNotOptArg, resolution=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg
			, arg4=defaultUnnamedArg):
		'Returns the data of the objects.'
		return self._oleobj_.InvokeTypes(21, LCID, 4, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 1)),dataType
			, resolution, Width, Height, arg4)

	def Unselect(self):
		'Unselects the objects in the parent.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'AltGroups' returns object of type 'IChemDrawAltGroups'
		"AltGroups": (309, 2, (9, 0), (), "AltGroups", '{D9E5D3D1-0D59-4126-B108-7D567E396FB3}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'Arrows' returns object of type 'IChemDrawArrows'
		"Arrows": (316, 2, (9, 0), (), "Arrows", '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}'),
		# Method 'Atoms' returns object of type 'IChemDrawAtoms'
		"Atoms": (301, 2, (9, 0), (), "Atoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'Bitmap' returns object of type 'Picture'
		"Bitmap": (33, 2, (9, 0), (), "Bitmap", '{7BF80981-BF32-101A-8BBB-00AA00300CAB}'),
		# Method 'Bonds' returns object of type 'IChemDrawBonds'
		"Bonds": (302, 2, (9, 0), (), "Bonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		"Bottom": (17, 2, (5, 0), (), "Bottom", None),
		# Method 'Brackets' returns object of type 'IChemDrawBrackets'
		"Brackets": (320, 2, (9, 0), (), "Brackets", '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}'),
		# Method 'Captions' returns object of type 'IChemDrawTexts'
		"Captions": (305, 2, (9, 0), (), "Captions", '{D156092E-1412-458C-BD6A-3CC171B56E63}'),
		# Method 'Constraints' returns object of type 'IChemDrawConstraints'
		"Constraints": (311, 2, (9, 0), (), "Constraints", '{990C82BE-55F2-49F2-B822-2E448C7FEC80}'),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Data": (21, 2, (12, 0), ((12, 17), (12, 17), (12, 17), (12, 17)), "Data", None),
		# Method 'DataObject' returns object of type 'DataObject'
		"DataObject": (27, 2, (9, 0), (), "DataObject", '{41A7D760-6018-11CF-9016-00AA0068841E}'),
		"ElementalAnalysis": (3, 2, (8, 0), (), "ElementalAnalysis", None),
		# Method 'EnhancedMetafile' returns object of type 'Picture'
		"EnhancedMetafile": (35, 2, (9, 0), (), "EnhancedMetafile", '{7BF80981-BF32-101A-8BBB-00AA00300CAB}'),
		"ExactMass": (4, 2, (5, 0), (), "ExactMass", None),
		"Formula": (5, 2, (8, 0), (), "Formula", None),
		"FormulaHTML": (41, 2, (8, 0), (), "FormulaHTML", None),
		# Method 'Geometries' returns object of type 'IChemDrawGeometries'
		"Geometries": (310, 2, (9, 0), (), "Geometries", '{53C77081-53BF-4397-9BB4-84D6AF7C10F3}'),
		# Method 'Graphics' returns object of type 'IChemDrawGraphics'
		"Graphics": (303, 2, (9, 0), (), "Graphics", '{D0E3D4B9-3B16-4331-BBA2-651319AE0402}'),
		# Method 'Groups' returns object of type 'IChemDrawGroups'
		"Groups": (307, 2, (9, 0), (), "Groups", '{E5164832-7AFC-463A-9C19-A1AF6D191020}'),
		"Height": (14, 2, (5, 0), (), "Height", None),
		"Left": (18, 2, (5, 0), (), "Left", None),
		# Method 'Metafile' returns object of type 'Picture'
		"Metafile": (34, 2, (9, 0), (), "Metafile", '{7BF80981-BF32-101A-8BBB-00AA00300CAB}'),
		"MolecularWeight": (6, 2, (5, 0), (), "MolecularWeight", None),
		"Parent": (7, 2, (9, 0), (), "Parent", None),
		# Method 'Pictures' returns object of type 'IChemDrawPictures'
		"Pictures": (306, 2, (9, 0), (), "Pictures", '{41652842-15D6-44AE-AEFF-B51B179CF019}'),
		# Method 'PlasmidMaps' returns object of type 'IChemDrawPlasmidMaps'
		"PlasmidMaps": (315, 2, (9, 0), (), "PlasmidMaps", '{E06B3507-3060-4095-8406-BAADD00A054E}'),
		# Method 'ReactionSchemes' returns object of type 'IChemDrawReactionSchemes'
		"ReactionSchemes": (312, 2, (9, 0), (), "ReactionSchemes", '{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}'),
		"Right": (19, 2, (5, 0), (), "Right", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (22, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		# Method 'Splines' returns object of type 'IChemDrawSplines'
		"Splines": (304, 2, (9, 0), (), "Splines", '{272423F1-2909-4340-8870-8062530ADD05}'),
		# Method 'StoichiometryGrids' returns object of type 'IChemDrawStoichiometryGrids'
		"StoichiometryGrids": (314, 2, (9, 0), (), "StoichiometryGrids", '{27109627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Symbols' returns object of type 'IChemDrawSymbols'
		"Symbols": (319, 2, (9, 0), (), "Symbols", '{D44C587D-2434-46B8-8B76-D309A2632456}'),
		# Method 'TLCPlates' returns object of type 'IChemDrawTLCPlates'
		"TLCPlates": (313, 2, (9, 0), (), "TLCPlates", '{27609627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Tables' returns object of type 'IChemDrawTables'
		"Tables": (308, 2, (9, 0), (), "Tables", '{80C78566-D4BF-460E-B055-5728877FB30E}'),
		"Top": (16, 2, (5, 0), (), "Top", None),
		"Width": (15, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Data": ((21, LCID, 4, 0),()),
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A341E650-F6F0-4068-B499-C231DDEBFBFD}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A341E650-F6F0-4068-B499-C231DDEBFBFD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawPicture(DispatchBaseClass):
	'ChemDraw picture interface'
	CLSID = IID('{108A38A7-A0A1-4534-B59B-FFAEBC96D489}')
	coclass_clsid = IID('{46CB2881-7626-4C35-A4D7-45F245CC8376}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		"PictureType": (101, 2, (3, 0), (), "PictureType", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawPictures(DispatchBaseClass):
	'ChemDraw pictures interface'
	CLSID = IID('{41652842-15D6-44AE-AEFF-B51B179CF019}')
	coclass_clsid = IID('{24535E40-072D-4068-AA42-154513415BB3}')

	# Result is of type IChemDrawPicture
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{108A38A7-A0A1-4534-B59B-FFAEBC96D489}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{108A38A7-A0A1-4534-B59B-FFAEBC96D489}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{108A38A7-A0A1-4534-B59B-FFAEBC96D489}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawPlasmidMap(DispatchBaseClass):
	'ChemDraw Plasmid Maps interface'
	CLSID = IID('{F06B3507-3060-4095-8406-CBBDD00A054E}')
	coclass_clsid = IID('{4B87F2A6-B4BD-4418-9610-0216BC7DC190}')

	def AddMarker(self, retval=defaultNamedNotOptArg):
		'Add a new marker to the Plasmid Map.'
		return self._ApplyTypes_(301, 1, (24, 0), ((16393, 3),), 'AddMarker', None,retval
			)

	def AddPlasmid(self, retval=defaultNamedNotOptArg):
		'Add a new plasmid to the Plasmid Map.'
		return self._ApplyTypes_(302, 1, (24, 0), ((16393, 3),), 'AddPlasmid', None,retval
			)

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'Markers' returns object of type 'IChemDrawPlasmidMarkers'
		"Markers": (101, 2, (9, 0), (), "Markers", '{ABCB3507-3060-4095-8406-B8BDD00A054E}'),
		"NumberBasePairs": (201, 2, (3, 0), (), "NumberBasePairs", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		# Method 'Origin' returns object of type 'IChemDrawPoint'
		"Origin": (203, 2, (9, 0), (), "Origin", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Plasmids' returns object of type 'IChemDrawPlasmidRegions'
		"Plasmids": (102, 2, (9, 0), (), "Plasmids", '{DEFB3507-3060-4095-8406-EEFDD00A054E}'),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Radius": (202, 2, (3, 0), (), "Radius", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"NumberBasePairs": ((201, LCID, 4, 0),()),
		"Origin": ((203, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Radius": ((202, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawPlasmidMaps(DispatchBaseClass):
	'ChemDraw PlasmidMaps interface'
	CLSID = IID('{E06B3507-3060-4095-8406-BAADD00A054E}')
	coclass_clsid = IID('{E2CB8432-6642-4DEB-B956-A6A579922E80}')

	# Result is of type IChemDrawPlasmidMap
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F06B3507-3060-4095-8406-CBBDD00A054E}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F06B3507-3060-4095-8406-CBBDD00A054E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F06B3507-3060-4095-8406-CBBDD00A054E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawPlasmidMarker(DispatchBaseClass):
	'ChemDraw Plasmid Marker interface'
	CLSID = IID('{F06B3507-3060-4095-8406-B8BDD00A054E}')
	coclass_clsid = IID('{DA5D0F99-162A-45B0-B81B-0F48A4781DE2}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"MarkerValue": (202, 2, (3, 0), (), "MarkerValue", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Offset": (203, 2, (3, 0), (), "Offset", None),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"MarkerValue": ((202, LCID, 4, 0),()),
		"Offset": ((203, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawPlasmidMarkers(DispatchBaseClass):
	'ChemDraw PlasmidMarkers interface'
	CLSID = IID('{ABCB3507-3060-4095-8406-B8BDD00A054E}')
	coclass_clsid = IID('{10840A43-1023-47A4-AD33-3C92B257DD61}')

	# Result is of type IChemDrawPlasmidMarker
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F06B3507-3060-4095-8406-B8BDD00A054E}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F06B3507-3060-4095-8406-B8BDD00A054E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F06B3507-3060-4095-8406-B8BDD00A054E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawPlasmidRegion(DispatchBaseClass):
	'ChemDraw Plasmid Region interface'
	CLSID = IID('{DEFB3507-3060-4095-8406-BBCDD00A054E}')
	coclass_clsid = IID('{E0D25ABD-8210-4390-AF26-EC7B85C651FA}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Offset": (203, 2, (3, 0), (), "Offset", None),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"RegionEnd": (202, 2, (3, 0), (), "RegionEnd", None),
		"RegionStart": (201, 2, (3, 0), (), "RegionStart", None),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Offset": ((203, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"RegionEnd": ((202, LCID, 4, 0),()),
		"RegionStart": ((201, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawPlasmidRegions(DispatchBaseClass):
	'ChemDraw PlasmidRegions interface'
	CLSID = IID('{DEFB3507-3060-4095-8406-EEFDD00A054E}')
	coclass_clsid = IID('{2193B148-381B-486E-B96B-B21C6CD6AD02}')

	# Result is of type IChemDrawPlasmidRegion
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DEFB3507-3060-4095-8406-BBCDD00A054E}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DEFB3507-3060-4095-8406-BBCDD00A054E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{DEFB3507-3060-4095-8406-BBCDD00A054E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawPoint(DispatchBaseClass):
	'ChemDraw point interface'
	CLSID = IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')
	coclass_clsid = IID('{A61082F6-DD43-4DF4-9B7C-C25B0024DB4D}')

	_prop_map_get_ = {
		"X": (1, 2, (5, 0), (), "X", None),
		"Y": (2, 2, (5, 0), (), "Y", None),
		"Z": (3, 2, (5, 0), (), "Z", None),
	}
	_prop_map_put_ = {
		"X": ((1, LCID, 4, 0),()),
		"Y": ((2, LCID, 4, 0),()),
		"Z": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawPreferences(DispatchBaseClass):
	'ChemDraw preferences interface -- these preferences affect every document'
	CLSID = IID('{4BC8155A-553E-4992-A555-FEEECB11CAB8}')
	coclass_clsid = IID('{7C97009F-5782-4C5B-8601-7784BDE3F73D}')

	_prop_map_get_ = {
		"AntialiasedGIFs": (24, 2, (11, 0), (), "AntialiasedGIFs", None),
		"AutoLassoSelection": (16, 2, (11, 0), (), "AutoLassoSelection", None),
		"AutoReactionMap": (10, 2, (11, 0), (), "AutoReactionMap", None),
		"AutoSave": (36, 2, (11, 0), (), "AutoSave", None),
		"AutoSaveMinutes": (37, 2, (3, 0), (), "AutoSaveMinutes", None),
		"AutomaticLabels": (5, 2, (11, 0), (), "AutomaticLabels", None),
		"CheckFileExtensionsWhenLaunching": (41, 2, (11, 0), (), "CheckFileExtensionsWhenLaunching", None),
		"CheckStructure": (7, 2, (11, 0), (), "CheckStructure", None),
		"ChemDrawItemsDirectory": (32, 2, (8, 0), (), "ChemDrawItemsDirectory", None),
		"ChemicalWarningsToShow": (27, 2, (3, 0), (), "ChemicalWarningsToShow", None),
		"DefaultToolWhenOpeningDocuments": (33, 2, (3, 0), (), "DefaultToolWhenOpeningDocuments", None),
		"DisablePerspectiveStereoPerception": (47, 2, (11, 0), (), "DisablePerspectiveStereoPerception", None),
		"DocumentsDirectory": (31, 2, (8, 0), (), "DocumentsDirectory", None),
		"EPSBondQuality": (60, 2, (3, 0), (), "EPSBondQuality", None),
		"EPSColor": (21, 2, (3, 0), (), "EPSColor", None),
		"EPSResolution": (22, 2, (3, 0), (), "EPSResolution", None),
		"FixedAngles": (14, 2, (11, 0), (), "FixedAngles", None),
		"FixedLengths": (13, 2, (11, 0), (), "FixedLengths", None),
		"FragmentationAnalyzerType": (44, 2, (3, 0), (), "FragmentationAnalyzerType", None),
		"FragmentationAutoUpdate": (46, 2, (11, 0), (), "FragmentationAutoUpdate", None),
		"FragmentationHighlightType": (45, 2, (3, 0), (), "FragmentationHighlightType", None),
		"GraphicsOutputBorder": (40, 2, (3, 0), (), "GraphicsOutputBorder", None),
		"HideAbsoluteStereoFlags": (56, 2, (11, 0), (), "HideAbsoluteStereoFlags", None),
		"IgnoreTopLevelChiralFlag": (59, 2, (11, 0), (), "IgnoreTopLevelChiralFlag", None),
		"IncludeDefaultFooter": (15, 2, (11, 0), (), "IncludeDefaultFooter", None),
		"NMRCSystemData": (51, 2, (11, 0), (), "NMRCSystemData", None),
		"NMRHFrequency": (42, 2, (3, 0), (), "NMRHFrequency", None),
		"NMRHSolvent": (48, 2, (3, 0), (), "NMRHSolvent", None),
		"NMRHSystemData": (49, 2, (11, 0), (), "NMRHSystemData", None),
		"NMRHUserData": (50, 2, (11, 0), (), "NMRHUserData", None),
		"OpenFormat": (29, 2, (3, 0), (), "OpenFormat", None),
		"PNGResolution": (43, 2, (3, 0), (), "PNGResolution", None),
		"PostScriptPreviewUsesTIFF": (26, 2, (11, 0), (), "PostScriptPreviewUsesTIFF", None),
		"PostScriptPreviewUsesWMF": (25, 2, (11, 0), (), "PostScriptPreviewUsesWMF", None),
		"PrintBackgroundColor": (6, 2, (11, 0), (), "PrintBackgroundColor", None),
		"PromptForComment": (38, 2, (11, 0), (), "PromptForComment", None),
		"RequireCtrlEnterCaption": (4, 2, (11, 0), (), "RequireCtrlEnterCaption", None),
		"RequireCtrlEnterLabel": (3, 2, (11, 0), (), "RequireCtrlEnterLabel", None),
		"RetainIUPACNumber": (53, 2, (11, 0), (), "RetainIUPACNumber", None),
		"SaveFormat": (35, 2, (3, 0), (), "SaveFormat", None),
		"ShowAttachmentRank": (8, 2, (11, 0), (), "ShowAttachmentRank", None),
		"ShowChemicalWarning": (12, 2, (11, 0), (), "ShowChemicalWarning", None),
		"ShowChiralInPlaceOfABS": (58, 2, (11, 0), (), "ShowChiralInPlaceOfABS", None),
		"ShowMDLTopLevelStereoFlags": (54, 2, (11, 0), (), "ShowMDLTopLevelStereoFlags", None),
		"ShowReactionMap": (9, 2, (11, 0), (), "ShowReactionMap", None),
		"ShowSlideGuides": (2, 2, (11, 0), (), "ShowSlideGuides", None),
		"ShowStereochemistry": (11, 2, (11, 0), (), "ShowStereochemistry", None),
		"SuppressSettingDefAbsESC": (57, 2, (11, 0), (), "SuppressSettingDefAbsESC", None),
		"TIFFColor": (18, 2, (3, 0), (), "TIFFColor", None),
		"TIFFCompression": (19, 2, (3, 0), (), "TIFFCompression", None),
		"TIFFResolution": (20, 2, (3, 0), (), "TIFFResolution", None),
		"Tolerance": (1, 2, (2, 0), (), "Tolerance", None),
		"TransparentGIFs": (23, 2, (11, 0), (), "TransparentGIFs", None),
		"TransparentPNGs": (52, 2, (11, 0), (), "TransparentPNGs", None),
		"Units": (17, 2, (3, 0), (), "Units", None),
		"UseDocumentsDirectory": (30, 2, (11, 0), (), "UseDocumentsDirectory", None),
		"UseESCForSKCFileFormat": (55, 2, (11, 0), (), "UseESCForSKCFileFormat", None),
		"UseOpenFormat": (28, 2, (11, 0), (), "UseOpenFormat", None),
		"UseSaveFormat": (34, 2, (11, 0), (), "UseSaveFormat", None),
		"WarnAboutDataLoss": (39, 2, (11, 0), (), "WarnAboutDataLoss", None),
	}
	_prop_map_put_ = {
		"AntialiasedGIFs": ((24, LCID, 4, 0),()),
		"AutoLassoSelection": ((16, LCID, 4, 0),()),
		"AutoReactionMap": ((10, LCID, 4, 0),()),
		"AutoSave": ((36, LCID, 4, 0),()),
		"AutoSaveMinutes": ((37, LCID, 4, 0),()),
		"AutomaticLabels": ((5, LCID, 4, 0),()),
		"CheckFileExtensionsWhenLaunching": ((41, LCID, 4, 0),()),
		"CheckStructure": ((7, LCID, 4, 0),()),
		"ChemDrawItemsDirectory": ((32, LCID, 4, 0),()),
		"ChemicalWarningsToShow": ((27, LCID, 4, 0),()),
		"DefaultToolWhenOpeningDocuments": ((33, LCID, 4, 0),()),
		"DisablePerspectiveStereoPerception": ((47, LCID, 4, 0),()),
		"DocumentsDirectory": ((31, LCID, 4, 0),()),
		"EPSBondQuality": ((60, LCID, 4, 0),()),
		"EPSColor": ((21, LCID, 4, 0),()),
		"EPSResolution": ((22, LCID, 4, 0),()),
		"FixedAngles": ((14, LCID, 4, 0),()),
		"FixedLengths": ((13, LCID, 4, 0),()),
		"FragmentationAnalyzerType": ((44, LCID, 4, 0),()),
		"FragmentationAutoUpdate": ((46, LCID, 4, 0),()),
		"FragmentationHighlightType": ((45, LCID, 4, 0),()),
		"GraphicsOutputBorder": ((40, LCID, 4, 0),()),
		"HideAbsoluteStereoFlags": ((56, LCID, 4, 0),()),
		"IgnoreTopLevelChiralFlag": ((59, LCID, 4, 0),()),
		"IncludeDefaultFooter": ((15, LCID, 4, 0),()),
		"NMRCSystemData": ((51, LCID, 4, 0),()),
		"NMRHFrequency": ((42, LCID, 4, 0),()),
		"NMRHSolvent": ((48, LCID, 4, 0),()),
		"NMRHSystemData": ((49, LCID, 4, 0),()),
		"NMRHUserData": ((50, LCID, 4, 0),()),
		"OpenFormat": ((29, LCID, 4, 0),()),
		"PNGResolution": ((43, LCID, 4, 0),()),
		"PostScriptPreviewUsesTIFF": ((26, LCID, 4, 0),()),
		"PostScriptPreviewUsesWMF": ((25, LCID, 4, 0),()),
		"PrintBackgroundColor": ((6, LCID, 4, 0),()),
		"PromptForComment": ((38, LCID, 4, 0),()),
		"RequireCtrlEnterCaption": ((4, LCID, 4, 0),()),
		"RequireCtrlEnterLabel": ((3, LCID, 4, 0),()),
		"RetainIUPACNumber": ((53, LCID, 4, 0),()),
		"SaveFormat": ((35, LCID, 4, 0),()),
		"ShowAttachmentRank": ((8, LCID, 4, 0),()),
		"ShowChemicalWarning": ((12, LCID, 4, 0),()),
		"ShowChiralInPlaceOfABS": ((58, LCID, 4, 0),()),
		"ShowMDLTopLevelStereoFlags": ((54, LCID, 4, 0),()),
		"ShowReactionMap": ((9, LCID, 4, 0),()),
		"ShowSlideGuides": ((2, LCID, 4, 0),()),
		"ShowStereochemistry": ((11, LCID, 4, 0),()),
		"SuppressSettingDefAbsESC": ((57, LCID, 4, 0),()),
		"TIFFColor": ((18, LCID, 4, 0),()),
		"TIFFCompression": ((19, LCID, 4, 0),()),
		"TIFFResolution": ((20, LCID, 4, 0),()),
		"Tolerance": ((1, LCID, 4, 0),()),
		"TransparentGIFs": ((23, LCID, 4, 0),()),
		"TransparentPNGs": ((52, LCID, 4, 0),()),
		"Units": ((17, LCID, 4, 0),()),
		"UseDocumentsDirectory": ((30, LCID, 4, 0),()),
		"UseESCForSKCFileFormat": ((55, LCID, 4, 0),()),
		"UseOpenFormat": ((28, LCID, 4, 0),()),
		"UseSaveFormat": ((34, LCID, 4, 0),()),
		"WarnAboutDataLoss": ((39, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawReactionScheme(DispatchBaseClass):
	'ChemDraw reaction scheme interface'
	CLSID = IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}')
	coclass_clsid = IID('{8BC99E8A-2E32-449B-A22F-BFBE43903E91}')

	_prop_map_get_ = {
		# Method 'Arrows' returns object of type 'IChemDrawArrows'
		"Arrows": (7, 2, (9, 0), (), "Arrows", '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}'),
		# Method 'Intermediates' returns object of type 'IChemDrawReactionStepComponents'
		"Intermediates": (5, 2, (9, 0), (), "Intermediates", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		# Method 'Plusses' returns object of type 'IChemDrawReactionStepComponents'
		"Plusses": (6, 2, (9, 0), (), "Plusses", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		# Method 'Products' returns object of type 'IChemDrawReactionStepComponents'
		"Products": (4, 2, (9, 0), (), "Products", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		# Method 'Reactants' returns object of type 'IChemDrawReactionStepComponents'
		"Reactants": (3, 2, (9, 0), (), "Reactants", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		"ReactionSchemeType": (2, 2, (3, 0), (), "ReactionSchemeType", None),
		# Method 'ReactionSteps' returns object of type 'IChemDrawReactionSteps'
		"ReactionSteps": (1, 2, (9, 0), (), "ReactionSteps", '{1AF22C1E-B493-4B09-93BF-CBF17E8E0C9E}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawReactionSchemes(DispatchBaseClass):
	'ChemDraw reaction schemes interface'
	CLSID = IID('{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}')
	coclass_clsid = IID('{C1782781-382B-4D8F-84F7-D94AD34299FC}')

	# Result is of type IChemDrawReactionScheme
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawReactionStep(DispatchBaseClass):
	'ChemDraw reaction step interface'
	CLSID = IID('{8CDB739E-0CC6-4801-9699-F75CED822069}')
	coclass_clsid = IID('{125A7E5F-B055-45E0-894E-BFB0405809F7}')

	_prop_map_get_ = {
		# Method 'Arrow' returns object of type 'IChemDrawArrow'
		"Arrow": (6, 2, (9, 0), (), "Arrow", '{669C0868-90B0-4469-9621-7639880698B1}'),
		# Method 'ObjectsAboveArrow' returns object of type 'IChemDrawReactionStepComponents'
		"ObjectsAboveArrow": (3, 2, (9, 0), (), "ObjectsAboveArrow", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		# Method 'ObjectsBelowArrow' returns object of type 'IChemDrawReactionStepComponents'
		"ObjectsBelowArrow": (4, 2, (9, 0), (), "ObjectsBelowArrow", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		# Method 'Plusses' returns object of type 'IChemDrawReactionStepComponents'
		"Plusses": (5, 2, (9, 0), (), "Plusses", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		# Method 'Products' returns object of type 'IChemDrawReactionStepComponents'
		"Products": (2, 2, (9, 0), (), "Products", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
		# Method 'Reactants' returns object of type 'IChemDrawReactionStepComponents'
		"Reactants": (1, 2, (9, 0), (), "Reactants", '{17E5A261-238D-44B1-BE44-704C63DF60DC}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawReactionStepComponents(DispatchBaseClass):
	'ChemDraw reaction step components interface'
	CLSID = IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')
	coclass_clsid = IID('{9A7B95B6-AA5B-4CC7-B996-D99989051F60}')

	# Result is of type IChemDrawObjects
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns a component in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns a component in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawReactionSteps(DispatchBaseClass):
	'ChemDraw reaction steps interface'
	CLSID = IID('{1AF22C1E-B493-4B09-93BF-CBF17E8E0C9E}')
	coclass_clsid = IID('{9F8EDE4B-1872-4ABE-9255-1F3A49703F3E}')

	# Result is of type IChemDrawReactionStep
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8CDB739E-0CC6-4801-9699-F75CED822069}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8CDB739E-0CC6-4801-9699-F75CED822069}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8CDB739E-0CC6-4801-9699-F75CED822069}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawRect(DispatchBaseClass):
	'ChemDraw rectangle interface'
	CLSID = IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')
	coclass_clsid = IID('{3A0F4F2C-92C7-4569-96B6-D608BCBAFD66}')

	def Deflate(self, dx=defaultNamedNotOptArg, dy=defaultNamedNotOptArg):
		'Subtract the specified amounts from the right and bottom edges, and add them to the left and top edges.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((5, 1), (5, 1)),dx
			, dy)

	def Inflate(self, dx=defaultNamedNotOptArg, dy=defaultNamedNotOptArg):
		'Add the specified amounts to the right and bottom edges, and subtract them from the left and top edges.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((5, 1), (5, 1)),dx
			, dy)

	def Intersection(self, newVal=defaultNamedNotOptArg):
		"Set this rectangle to the intersection of its area and another rectangle's area."
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((9, 1),),newVal
			)

	def IsWithin(self, newVal=defaultNamedNotOptArg):
		'Returns true if the area of this rectangle is completely contained within the area of the other rectangle.'
		return self._oleobj_.InvokeTypes(107, LCID, 1, (11, 0), ((9, 1),),newVal
			)

	def Offset(self, dx=defaultNamedNotOptArg, dy=defaultNamedNotOptArg):
		'Shift the rectangle by the specified amount.'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), ((5, 1), (5, 1)),dx
			, dy)

	def Overlaps(self, newVal=defaultNamedNotOptArg):
		'Returns true if the intersection of this rectangle and another rectangle is non-empty.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (11, 0), ((9, 1),),newVal
			)

	def PtInRect(self, newVal=defaultNamedNotOptArg):
		'Returns true if the point is within the bounds of the rectangle.'
		return self._oleobj_.InvokeTypes(108, LCID, 1, (11, 0), ((9, 1),),newVal
			)

	def Union(self, newVal=defaultNamedNotOptArg):
		"Set this rectangle to the union of its area and another rectangle's area."
		return self._oleobj_.InvokeTypes(106, LCID, 1, (24, 0), ((9, 1),),newVal
			)

	_prop_map_get_ = {
		"Bottom": (3, 2, (5, 0), (), "Bottom", None),
		# Method 'BottomLeft' returns object of type 'IChemDrawPoint'
		"BottomLeft": (9, 2, (9, 0), (), "BottomLeft", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'BottomRight' returns object of type 'IChemDrawPoint'
		"BottomRight": (10, 2, (9, 0), (), "BottomRight", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'Center' returns object of type 'IChemDrawPoint'
		"Center": (11, 2, (9, 0), (), "Center", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Height": (6, 2, (5, 0), (), "Height", None),
		"IsEmpty": (13, 2, (11, 0), (), "IsEmpty", None),
		"Left": (2, 2, (5, 0), (), "Left", None),
		"Right": (4, 2, (5, 0), (), "Right", None),
		"Top": (1, 2, (5, 0), (), "Top", None),
		# Method 'TopLeft' returns object of type 'IChemDrawPoint'
		"TopLeft": (7, 2, (9, 0), (), "TopLeft", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'TopRight' returns object of type 'IChemDrawPoint'
		"TopRight": (8, 2, (9, 0), (), "TopRight", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Width": (5, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Bottom": ((3, LCID, 4, 0),()),
		"BottomLeft": ((9, LCID, 4, 0),()),
		"BottomRight": ((10, LCID, 4, 0),()),
		"Center": ((11, LCID, 4, 0),()),
		"Height": ((6, LCID, 4, 0),()),
		"Left": ((2, LCID, 4, 0),()),
		"Right": ((4, LCID, 4, 0),()),
		"Top": ((1, LCID, 4, 0),()),
		"TopLeft": ((7, LCID, 4, 0),()),
		"TopRight": ((8, LCID, 4, 0),()),
		"Width": ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawSGComponent(DispatchBaseClass):
	'ChemDraw Stoichiometry Grid component interface'
	CLSID = IID('{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}')
	coclass_clsid = IID('{22144C17-01EC-471D-B15E-C40090786B54}')

	def AddProperty(self, retval=defaultNamedNotOptArg):
		'Add a new property to the component.'
		return self._ApplyTypes_(201, 1, (24, 0), ((16393, 3),), 'AddProperty', None,retval
			)

	_prop_map_get_ = {
		# Method 'Properties' returns object of type 'IChemDrawSGProperties'
		"Properties": (101, 2, (9, 0), (), "Properties", '{2214F33B-47B7-4CD8-AC4D-1906F3719D70}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawSGComponents(DispatchBaseClass):
	'ChemDraw Stoichiometry Grid Components interface'
	CLSID = IID('{BE1EA86E-C241-43B1-892B-05771CA47928}')
	coclass_clsid = IID('{BE1FFDC2-A4B8-4B8E-99C9-9AB476904B5F}')

	# Result is of type IChemDrawSGComponent
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawSGProperties(DispatchBaseClass):
	'ChemDraw Stoichiometry Grid Properties interface'
	CLSID = IID('{2214F33B-47B7-4CD8-AC4D-1906F3719D70}')
	coclass_clsid = IID('{181B972B-956D-4A92-BEDE-6B81D3232694}')

	# Result is of type IChemDrawSGProperty
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawSGProperty(DispatchBaseClass):
	'ChemDraw Stoichiometry Grid Property interface'
	CLSID = IID('{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}')
	coclass_clsid = IID('{D41B5DF8-89D0-4D7B-9811-F510AECB6798}')

	_prop_map_get_ = {
		"Color": (10, 2, (19, 0), (), "Color", None),
		"ID": (1, 2, (3, 0), (), "ID", None),
		# Method 'Text' returns object of type 'IChemDrawObjectTag'
		"Text": (13, 2, (9, 0), (), "Text", '{6DA748D4-4F21-45EA-BF09-F493643180F0}'),
	}
	_prop_map_put_ = {
		"Color": ((10, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawSelection(DispatchBaseClass):
	'ChemDraw Selection interface'
	CLSID = IID('{2590DD54-2A58-4A2A-AF35-5EE4CE3EABFA}')
	coclass_clsid = IID('{7AF6DD12-F154-4FAE-8437-3B51CD00A5DE}')

	_prop_map_get_ = {
		# Method 'AltGroups' returns object of type 'IChemDrawAltGroups'
		"AltGroups": (309, 2, (9, 0), (), "AltGroups", '{D9E5D3D1-0D59-4126-B108-7D567E396FB3}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'Arrows' returns object of type 'IChemDrawArrows'
		"Arrows": (316, 2, (9, 0), (), "Arrows", '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}'),
		# Method 'Atoms' returns object of type 'IChemDrawAtoms'
		"Atoms": (301, 2, (9, 0), (), "Atoms", '{4A2B95A2-2332-433B-B081-39A2B87C781E}'),
		# Method 'Bonds' returns object of type 'IChemDrawBonds'
		"Bonds": (302, 2, (9, 0), (), "Bonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		# Method 'Brackets' returns object of type 'IChemDrawBrackets'
		"Brackets": (320, 2, (9, 0), (), "Brackets", '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}'),
		# Method 'Captions' returns object of type 'IChemDrawTexts'
		"Captions": (305, 2, (9, 0), (), "Captions", '{D156092E-1412-458C-BD6A-3CC171B56E63}'),
		# Method 'Constraints' returns object of type 'IChemDrawConstraints'
		"Constraints": (311, 2, (9, 0), (), "Constraints", '{990C82BE-55F2-49F2-B822-2E448C7FEC80}'),
		# Method 'DataObject' returns object of type 'DataObject'
		"DataObject": (2, 2, (9, 0), (), "DataObject", '{41A7D760-6018-11CF-9016-00AA0068841E}'),
		# Method 'Geometries' returns object of type 'IChemDrawGeometries'
		"Geometries": (310, 2, (9, 0), (), "Geometries", '{53C77081-53BF-4397-9BB4-84D6AF7C10F3}'),
		# Method 'Graphics' returns object of type 'IChemDrawGraphics'
		"Graphics": (303, 2, (9, 0), (), "Graphics", '{D0E3D4B9-3B16-4331-BBA2-651319AE0402}'),
		# Method 'Groups' returns object of type 'IChemDrawGroups'
		"Groups": (307, 2, (9, 0), (), "Groups", '{E5164832-7AFC-463A-9C19-A1AF6D191020}'),
		# Method 'Objects' returns object of type 'IChemDrawObjects'
		"Objects": (3, 2, (9, 0), (), "Objects", '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Pictures' returns object of type 'IChemDrawPictures'
		"Pictures": (306, 2, (9, 0), (), "Pictures", '{41652842-15D6-44AE-AEFF-B51B179CF019}'),
		# Method 'PlasmidMaps' returns object of type 'IChemDrawPlasmidMaps'
		"PlasmidMaps": (315, 2, (9, 0), (), "PlasmidMaps", '{E06B3507-3060-4095-8406-BAADD00A054E}'),
		# Method 'ReactionSchemes' returns object of type 'IChemDrawReactionSchemes'
		"ReactionSchemes": (312, 2, (9, 0), (), "ReactionSchemes", '{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}'),
		# Method 'Splines' returns object of type 'IChemDrawSplines'
		"Splines": (304, 2, (9, 0), (), "Splines", '{272423F1-2909-4340-8870-8062530ADD05}'),
		# Method 'StoichiometryGrids' returns object of type 'IChemDrawStoichiometryGrids'
		"StoichiometryGrids": (314, 2, (9, 0), (), "StoichiometryGrids", '{27109627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Symbols' returns object of type 'IChemDrawSymbols'
		"Symbols": (319, 2, (9, 0), (), "Symbols", '{D44C587D-2434-46B8-8B76-D309A2632456}'),
		# Method 'TLCPlates' returns object of type 'IChemDrawTLCPlates'
		"TLCPlates": (313, 2, (9, 0), (), "TLCPlates", '{27609627-9196-4F73-8D89-25FC8B9C9592}'),
		# Method 'Tables' returns object of type 'IChemDrawTables'
		"Tables": (308, 2, (9, 0), (), "Tables", '{80C78566-D4BF-460E-B055-5728877FB30E}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawSettings(DispatchBaseClass):
	'ChemDraw settings interface -- settings that affect individual documents'
	CLSID = IID('{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}')
	coclass_clsid = IID('{290E5D0A-000C-405D-8E83-895CC9E3D8C4}')

	def ApplySettings(self, dataType=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg):
		'Change all the settings at once based on a file.'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (24, 0), ((12, 1), (12, 1)),dataType
			, newVal)

	_prop_map_get_ = {
		"AminoAcidTermini": (32, 2, (3, 0), (), "AminoAcidTermini", None),
		"BackgroundColor": (26, 2, (19, 0), (), "BackgroundColor", None),
		"BoldWidth": (6, 2, (5, 0), (), "BoldWidth", None),
		"BondLength": (4, 2, (5, 0), (), "BondLength", None),
		"BondSpacing": (2, 2, (5, 0), (), "BondSpacing", None),
		"CaptionFace": (15, 2, (2, 0), (), "CaptionFace", None),
		"CaptionFont": (13, 2, (8, 0), (), "CaptionFont", None),
		"CaptionJustification": (16, 2, (3, 0), (), "CaptionJustification", None),
		"CaptionLineHeight": (17, 2, (5, 0), (), "CaptionLineHeight", None),
		"CaptionSize": (14, 2, (5, 0), (), "CaptionSize", None),
		"ChainAngle": (1, 2, (2, 0), (), "ChainAngle", None),
		"Color": (25, 2, (19, 0), (), "Color", None),
		"HashSpacing": (3, 2, (5, 0), (), "HashSpacing", None),
		"HideImplicitHydrogens": (30, 2, (11, 0), (), "HideImplicitHydrogens", None),
		"InterpretChemically": (18, 2, (11, 0), (), "InterpretChemically", None),
		"LabelFace": (10, 2, (2, 0), (), "LabelFace", None),
		"LabelFont": (8, 2, (8, 0), (), "LabelFont", None),
		"LabelJustification": (11, 2, (3, 0), (), "LabelJustification", None),
		"LabelLineHeight": (12, 2, (5, 0), (), "LabelLineHeight", None),
		"LabelSize": (9, 2, (5, 0), (), "LabelSize", None),
		"LineWidth": (5, 2, (5, 0), (), "LineWidth", None),
		"MarginWidth": (7, 2, (5, 0), (), "MarginWidth", None),
		"ResidueBlockCount": (36, 2, (2, 0), (), "ResidueBlockCount", None),
		"ResidueWrapCount": (35, 2, (2, 0), (), "ResidueWrapCount", None),
		"ShowAtomEnhancedStereo": (31, 2, (11, 0), (), "ShowAtomEnhancedStereo", None),
		"ShowAtomNumber": (21, 2, (11, 0), (), "ShowAtomNumber", None),
		"ShowAtomQuery": (19, 2, (11, 0), (), "ShowAtomQuery", None),
		"ShowAtomStereo": (20, 2, (11, 0), (), "ShowAtomStereo", None),
		"ShowBondQuery": (22, 2, (11, 0), (), "ShowBondQuery", None),
		"ShowBondRxn": (24, 2, (11, 0), (), "ShowBondRxn", None),
		"ShowBondStereo": (23, 2, (11, 0), (), "ShowBondStereo", None),
		"ShowNonTerminalCarbonLabels": (29, 2, (11, 0), (), "ShowNonTerminalCarbonLabels", None),
		"ShowSequenceBonds": (34, 2, (11, 0), (), "ShowSequenceBonds", None),
		"ShowSequenceTermini": (33, 2, (11, 0), (), "ShowSequenceTermini", None),
		"ShowSequenceUnlinkedBranches": (39, 2, (11, 0), (), "ShowSequenceUnlinkedBranches", None),
		"ShowTerminalCarbonLabels": (28, 2, (11, 0), (), "ShowTerminalCarbonLabels", None),
	}
	_prop_map_put_ = {
		"AminoAcidTermini": ((32, LCID, 4, 0),()),
		"BackgroundColor": ((26, LCID, 4, 0),()),
		"BoldWidth": ((6, LCID, 4, 0),()),
		"BondLength": ((4, LCID, 4, 0),()),
		"BondSpacing": ((2, LCID, 4, 0),()),
		"CaptionFace": ((15, LCID, 4, 0),()),
		"CaptionFont": ((13, LCID, 4, 0),()),
		"CaptionJustification": ((16, LCID, 4, 0),()),
		"CaptionLineHeight": ((17, LCID, 4, 0),()),
		"CaptionSize": ((14, LCID, 4, 0),()),
		"ChainAngle": ((1, LCID, 4, 0),()),
		"Color": ((25, LCID, 4, 0),()),
		"HashSpacing": ((3, LCID, 4, 0),()),
		"HideImplicitHydrogens": ((30, LCID, 4, 0),()),
		"InterpretChemically": ((18, LCID, 4, 0),()),
		"LabelFace": ((10, LCID, 4, 0),()),
		"LabelFont": ((8, LCID, 4, 0),()),
		"LabelJustification": ((11, LCID, 4, 0),()),
		"LabelLineHeight": ((12, LCID, 4, 0),()),
		"LabelSize": ((9, LCID, 4, 0),()),
		"LineWidth": ((5, LCID, 4, 0),()),
		"MarginWidth": ((7, LCID, 4, 0),()),
		"ResidueBlockCount": ((36, LCID, 4, 0),()),
		"ResidueWrapCount": ((35, LCID, 4, 0),()),
		"ShowAtomEnhancedStereo": ((31, LCID, 4, 0),()),
		"ShowAtomNumber": ((21, LCID, 4, 0),()),
		"ShowAtomQuery": ((19, LCID, 4, 0),()),
		"ShowAtomStereo": ((20, LCID, 4, 0),()),
		"ShowBondQuery": ((22, LCID, 4, 0),()),
		"ShowBondRxn": ((24, LCID, 4, 0),()),
		"ShowBondStereo": ((23, LCID, 4, 0),()),
		"ShowNonTerminalCarbonLabels": ((29, LCID, 4, 0),()),
		"ShowSequenceBonds": ((34, LCID, 4, 0),()),
		"ShowSequenceTermini": ((33, LCID, 4, 0),()),
		"ShowSequenceUnlinkedBranches": ((39, LCID, 4, 0),()),
		"ShowTerminalCarbonLabels": ((28, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawSpline(DispatchBaseClass):
	'ChemDraw spline interface'
	CLSID = IID('{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')
	coclass_clsid = IID('{FEDAEFD6-F32A-40A8-97D5-8E5DF32425B3}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawPoint
	def GetPoint(self, index=defaultNamedNotOptArg):
		'Given an index, returns that point used to describe the spline.'
		ret = self._oleobj_.InvokeTypes(102, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPoint', '{16E2B1FC-50AE-4226-A471-F4029D444BA3}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	def SetPoint(self, index=defaultNamedNotOptArg, newVal=defaultNamedNotOptArg):
		'Given an index, sets that point used to describe the spline.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((3, 1), (9, 1)),index
			, newVal)

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"ArrowHeadPositionAtEnd": (107, 2, (3, 0), (), "ArrowHeadPositionAtEnd", None),
		"ArrowHeadPositionAtStart": (106, 2, (3, 0), (), "ArrowHeadPositionAtStart", None),
		"ArrowHeadType": (105, 2, (3, 0), (), "ArrowHeadType", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'DelocalizedBonds' returns object of type 'IChemDrawBonds'
		"DelocalizedBonds": (104, 2, (9, 0), (), "DelocalizedBonds", '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}'),
		"FillType": (115, 2, (3, 0), (), "FillType", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"HeadCenterSize": (111, 2, (5, 0), (), "HeadCenterSize", None),
		"HeadSize": (110, 2, (5, 0), (), "HeadSize", None),
		"HeadWidth": (112, 2, (5, 0), (), "HeadWidth", None),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"IsBold": (108, 2, (11, 0), (), "IsBold", None),
		"IsDashed": (109, 2, (11, 0), (), "IsDashed", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"LineType": (114, 2, (3, 0), (), "LineType", None),
		"NumPoints": (101, 2, (3, 0), (), "NumPoints", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Spacing": (113, 2, (5, 0), (), "Spacing", None),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"ArrowHeadPositionAtEnd": ((107, LCID, 4, 0),()),
		"ArrowHeadPositionAtStart": ((106, LCID, 4, 0),()),
		"ArrowHeadType": ((105, LCID, 4, 0),()),
		"Color": ((5, LCID, 4, 0),()),
		"FillType": ((115, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"HeadCenterSize": ((111, LCID, 4, 0),()),
		"HeadSize": ((110, LCID, 4, 0),()),
		"HeadWidth": ((112, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"IsBold": ((108, LCID, 4, 0),()),
		"IsDashed": ((109, LCID, 4, 0),()),
		"LineType": ((114, LCID, 4, 0),()),
		"NumPoints": ((101, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Spacing": ((113, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawSplines(DispatchBaseClass):
	'ChemDraw splines interface'
	CLSID = IID('{272423F1-2909-4340-8870-8062530ADD05}')
	coclass_clsid = IID('{31D1265E-BF76-43FE-A7B0-257325B904B3}')

	# Result is of type IChemDrawSpline
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawStoichiometryGrid(DispatchBaseClass):
	'ChemDraw Stoichiometry Grid interface'
	CLSID = IID('{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')
	coclass_clsid = IID('{1018F877-126F-44EB-8C26-D3A3E5286956}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Components' returns object of type 'IChemDrawSGComponents'
		"Components": (101, 2, (9, 0), (), "Components", '{BE1EA86E-C241-43B1-892B-05771CA47928}'),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawStoichiometryGrids(DispatchBaseClass):
	'ChemDraw Stoichiometry Grids interface'
	CLSID = IID('{27109627-9196-4F73-8D89-25FC8B9C9592}')
	coclass_clsid = IID('{F51EC5B2-1756-455F-9F1F-59188D877D20}')

	# Result is of type IChemDrawStoichiometryGrid
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawSymbol(DispatchBaseClass):
	'ChemDraw symbol object interface'
	CLSID = IID('{0C9366BF-36BB-4303-86FA-966657FF891D}')
	coclass_clsid = IID('{2984EE75-82FC-46B2-AE1E-8A82C77F2DE1}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'End' returns object of type 'IChemDrawPoint'
		"End": (102, 2, (9, 0), (), "End", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"IsCharge": (105, 2, (11, 0), (), "IsCharge", None),
		"IsNegativeCharge": (107, 2, (11, 0), (), "IsNegativeCharge", None),
		"IsPositiveCharge": (106, 2, (11, 0), (), "IsPositiveCharge", None),
		"IsRadical": (104, 2, (11, 0), (), "IsRadical", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		# Method 'Start' returns object of type 'IChemDrawPoint'
		"Start": (101, 2, (9, 0), (), "Start", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"SymbolType": (103, 2, (3, 0), (), "SymbolType", None),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"End": ((102, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Start": ((101, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawSymbols(DispatchBaseClass):
	'ChemDraw symbol objects interface'
	CLSID = IID('{D44C587D-2434-46B8-8B76-D309A2632456}')
	coclass_clsid = IID('{2470A7A4-3845-4AE3-8034-82F091367BF4}')

	# Result is of type IChemDrawSymbol
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0C9366BF-36BB-4303-86FA-966657FF891D}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0C9366BF-36BB-4303-86FA-966657FF891D}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{0C9366BF-36BB-4303-86FA-966657FF891D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawTLCLane(DispatchBaseClass):
	'ChemDraw TLC Lane interface'
	CLSID = IID('{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}')
	coclass_clsid = IID('{22B44C17-01EC-471D-B15E-C40090786B54}')

	def AddSpot(self, retval=defaultNamedNotOptArg):
		'Add a new spot to the TLC lane.'
		return self._ApplyTypes_(201, 1, (24, 0), ((16393, 3),), 'AddSpot', None,retval
			)

	_prop_map_get_ = {
		# Method 'Spots' returns object of type 'IChemDrawTLCSpots'
		"Spots": (101, 2, (9, 0), (), "Spots", '{2224F33B-47B7-4CD8-AC4D-1906F3719D70}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawTLCLanes(DispatchBaseClass):
	'ChemDraw TLC Lanes interface'
	CLSID = IID('{BEDEA86E-C241-43B1-892B-05771CA47928}')
	coclass_clsid = IID('{BE7FFDC2-A4B8-4B8E-99C9-9AB476904B5F}')

	# Result is of type IChemDrawTLCLane
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawTLCPlate(DispatchBaseClass):
	'ChemDraw TLC Plate interface'
	CLSID = IID('{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')
	coclass_clsid = IID('{1098F877-126F-44EB-8C26-D3A3E5286956}')

	def AddLane(self, retval=defaultNamedNotOptArg):
		'Add a new lane to the TLC plate.'
		return self._ApplyTypes_(201, 1, (24, 0), ((16393, 3),), 'AddLane', None,retval
			)

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'BottomLeft' returns object of type 'IChemDrawPoint'
		"BottomLeft": (104, 2, (9, 0), (), "BottomLeft", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'BottomRight' returns object of type 'IChemDrawPoint'
		"BottomRight": (105, 2, (9, 0), (), "BottomRight", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		# Method 'Lanes' returns object of type 'IChemDrawTLCLanes'
		"Lanes": (101, 2, (9, 0), (), "Lanes", '{BEDEA86E-C241-43B1-892B-05771CA47928}'),
		"Left": (17, 2, (5, 0), (), "Left", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"OriginFraction": (106, 2, (5, 0), (), "OriginFraction", None),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"ShowBorders": (110, 2, (11, 0), (), "ShowBorders", None),
		"ShowOrigin": (108, 2, (11, 0), (), "ShowOrigin", None),
		"ShowSideTicks": (111, 2, (11, 0), (), "ShowSideTicks", None),
		"ShowSolventFront": (109, 2, (11, 0), (), "ShowSolventFront", None),
		"SolventFrontFraction": (107, 2, (5, 0), (), "SolventFrontFraction", None),
		"Top": (15, 2, (5, 0), (), "Top", None),
		# Method 'TopLeft' returns object of type 'IChemDrawPoint'
		"TopLeft": (102, 2, (9, 0), (), "TopLeft", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		# Method 'TopRight' returns object of type 'IChemDrawPoint'
		"TopRight": (103, 2, (9, 0), (), "TopRight", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Transparent": (112, 2, (11, 0), (), "Transparent", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"BottomLeft": ((104, LCID, 4, 0),()),
		"BottomRight": ((105, LCID, 4, 0),()),
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"OriginFraction": ((106, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"ShowBorders": ((110, LCID, 4, 0),()),
		"ShowOrigin": ((108, LCID, 4, 0),()),
		"ShowSideTicks": ((111, LCID, 4, 0),()),
		"ShowSolventFront": ((109, LCID, 4, 0),()),
		"SolventFrontFraction": ((107, LCID, 4, 0),()),
		"TopLeft": ((102, LCID, 4, 0),()),
		"TopRight": ((103, LCID, 4, 0),()),
		"Transparent": ((112, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawTLCPlates(DispatchBaseClass):
	'ChemDraw TLC Plates interface'
	CLSID = IID('{27609627-9196-4F73-8D89-25FC8B9C9592}')
	coclass_clsid = IID('{F5EEC5B2-1756-455F-9F1F-59188D877D20}')

	# Result is of type IChemDrawTLCPlate
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawTLCSpot(DispatchBaseClass):
	'ChemDraw TLC Spot interface'
	CLSID = IID('{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}')
	coclass_clsid = IID('{D43B5DF8-89D0-4D7B-9811-F510AECB6798}')

	_prop_map_get_ = {
		"Bold": (6, 2, (11, 0), (), "Bold", None),
		"Color": (10, 2, (19, 0), (), "Color", None),
		"Dashed": (7, 2, (11, 0), (), "Dashed", None),
		"Filled": (8, 2, (11, 0), (), "Filled", None),
		"Height": (4, 2, (5, 0), (), "Height", None),
		"ID": (1, 2, (3, 0), (), "ID", None),
		"Rf": (2, 2, (5, 0), (), "Rf", None),
		# Method 'RfTag' returns object of type 'IChemDrawObjectTag'
		"RfTag": (13, 2, (9, 0), (), "RfTag", '{6DA748D4-4F21-45EA-BF09-F493643180F0}'),
		"ShowRf": (12, 2, (11, 0), (), "ShowRf", None),
		"Spacing": (9, 2, (5, 0), (), "Spacing", None),
		"Tail": (5, 2, (5, 0), (), "Tail", None),
		"Visible": (11, 2, (11, 0), (), "Visible", None),
		"Width": (3, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Bold": ((6, LCID, 4, 0),()),
		"Color": ((10, LCID, 4, 0),()),
		"Dashed": ((7, LCID, 4, 0),()),
		"Filled": ((8, LCID, 4, 0),()),
		"Height": ((4, LCID, 4, 0),()),
		"Rf": ((2, LCID, 4, 0),()),
		"ShowRf": ((12, LCID, 4, 0),()),
		"Spacing": ((9, LCID, 4, 0),()),
		"Tail": ((5, LCID, 4, 0),()),
		"Visible": ((11, LCID, 4, 0),()),
		"Width": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawTLCSpots(DispatchBaseClass):
	'ChemDraw TLC Spots interface'
	CLSID = IID('{2224F33B-47B7-4CD8-AC4D-1906F3719D70}')
	coclass_clsid = IID('{188B972B-956D-4A92-BEDE-6B81D3232694}')

	# Result is of type IChemDrawTLCSpot
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawTable(DispatchBaseClass):
	'ChemDraw table interface'
	CLSID = IID('{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')
	coclass_clsid = IID('{A803FB2E-9C62-4E72-8742-418C8892B15F}')

	def AddColumn(self, newColumnNum=defaultNamedNotOptArg):
		'Adds a new column at the specified position.'
		return self._oleobj_.InvokeTypes(103, LCID, 1, (24, 0), ((3, 1),),newColumnNum
			)

	def AddRow(self, newRowNum=defaultNamedNotOptArg):
		'Adds a new row at the specified position.'
		return self._oleobj_.InvokeTypes(102, LCID, 1, (24, 0), ((3, 1),),newRowNum
			)

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	def DeleteColumn(self, columnNum=defaultNamedNotOptArg):
		'Deletes the column at the specified position.'
		return self._oleobj_.InvokeTypes(105, LCID, 1, (24, 0), ((3, 1),),columnNum
			)

	def DeleteRow(self, rowNum=defaultNamedNotOptArg):
		'Deletes the row at the specified position.'
		return self._oleobj_.InvokeTypes(104, LCID, 1, (24, 0), ((3, 1),),rowNum
			)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		# Method 'Cells' returns object of type 'IChemDrawCells'
		"Cells": (101, 2, (9, 0), (), "Cells", '{26B98B2C-EE16-49FD-95E5-A8551149C0EF}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"NumColumns": (107, 2, (3, 0), (), "NumColumns", None),
		"NumRows": (106, 2, (3, 0), (), "NumRows", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawTables(DispatchBaseClass):
	'ChemDraw tables interface'
	CLSID = IID('{80C78566-D4BF-460E-B055-5728877FB30E}')
	coclass_clsid = IID('{DA47E69C-6A9A-4C52-8754-0158EC317F39}')

	# Result is of type IChemDrawTable
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawText(DispatchBaseClass):
	'ChemDraw caption interface'
	CLSID = IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')
	coclass_clsid = IID('{9B1B67CB-9794-4432-8F2D-766ED39AB5C4}')

	def Delete(self):
		'Deletes the object from the document.'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), (),)

	# Result is of type IChemDrawObjectTag
	def GetObjectTag(self, name=defaultNamedNotOptArg):
		'Returns a specified object tag.'
		ret = self._oleobj_.InvokeTypes(23, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	# Result is of type IChemDrawObjectTag
	def MakeObjectTag(self, name=defaultNamedNotOptArg, duplicatesAllowed=defaultNamedNotOptArg):
		'Adds a specified object tag to the object.'
		ret = self._oleobj_.InvokeTypes(24, LCID, 1, (9, 0), ((8, 1), (11, 1)),name
			, duplicatesAllowed)
		if ret is not None:
			ret = Dispatch(ret, 'MakeObjectTag', '{6DA748D4-4F21-45EA-BF09-F493643180F0}')
		return ret

	_prop_map_get_ = {
		"Angle": (103, 2, (5, 0), (), "Angle", None),
		# Method 'Annotations' returns object of type 'IChemDrawAnnotations'
		"Annotations": (26, 2, (9, 0), (), "Annotations", '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}'),
		"Application": (1, 2, (9, 0), (), "Application", None),
		# Method 'Atom' returns object of type 'IChemDrawAtom'
		"Atom": (108, 2, (9, 0), (), "Atom", '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}'),
		"Bottom": (16, 2, (5, 0), (), "Bottom", None),
		# Method 'Bounds' returns object of type 'IChemDrawRect'
		"Bounds": (11, 2, (9, 0), (), "Bounds", '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}'),
		"ChemicalWarning": (25, 2, (8, 0), (), "ChemicalWarning", None),
		"Color": (5, 2, (19, 0), (), "Color", None),
		"Face": (111, 2, (3, 0), (), "Face", None),
		"Family": (109, 2, (8, 0), (), "Family", None),
		# Method 'Fragment' returns object of type 'IChemDrawGroup'
		"Fragment": (21, 2, (9, 0), (), "Fragment", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		# Method 'Group' returns object of type 'IChemDrawGroup'
		"Group": (20, 2, (9, 0), (), "Group", '{40957F2E-AC2D-44B4-B237-A7E2A825E636}'),
		"Height": (13, 2, (5, 0), (), "Height", None),
		"Highlighted": (2, 2, (11, 0), (), "Highlighted", None),
		"ID": (3, 2, (3, 0), (), "ID", None),
		"IsCharge": (107, 2, (11, 0), (), "IsCharge", None),
		"IsEmpty": (106, 2, (11, 0), (), "IsEmpty", None),
		"Justification": (105, 2, (3, 0), (), "Justification", None),
		"Left": (17, 2, (5, 0), (), "Left", None),
		"LineHeight": (112, 2, (3, 0), (), "LineHeight", None),
		# Method 'ObjectTags' returns object of type 'IChemDrawObjectTags'
		"ObjectTags": (22, 2, (9, 0), (), "ObjectTags", '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}'),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		# Method 'Position' returns object of type 'IChemDrawPoint'
		"Position": (12, 2, (9, 0), (), "Position", '{16E2B1FC-50AE-4226-A471-F4029D444BA3}'),
		"Right": (18, 2, (5, 0), (), "Right", None),
		"Selected": (6, 2, (11, 0), (), "Selected", None),
		# Method 'Settings' returns object of type 'IChemDrawSettings'
		"Settings": (9, 2, (9, 0), (), "Settings", '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}'),
		"Size": (110, 2, (5, 0), (), "Size", None),
		# Method 'Styles' returns object of type 'IChemDrawTextStyles'
		"Styles": (102, 2, (9, 0), (), "Styles", '{B27DB485-6C90-45D2-82C1-7D2F55D73654}'),
		"Text": (101, 2, (8, 0), (), "Text", None),
		"Top": (15, 2, (5, 0), (), "Top", None),
		"Visible": (7, 2, (11, 0), (), "Visible", None),
		"WarningsIgnored": (10, 2, (11, 0), (), "WarningsIgnored", None),
		"Width": (14, 2, (5, 0), (), "Width", None),
		"WrapWidth": (104, 2, (5, 0), (), "WrapWidth", None),
		"index": (8, 2, (3, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Angle": ((103, LCID, 4, 0),()),
		"Atom": ((108, LCID, 4, 0),()),
		"Color": ((5, LCID, 4, 0),()),
		"Face": ((111, LCID, 4, 0),()),
		"Family": ((109, LCID, 4, 0),()),
		"Fragment": ((21, LCID, 4, 0),()),
		"Group": ((20, LCID, 4, 0),()),
		"Highlighted": ((2, LCID, 4, 0),()),
		"Justification": ((105, LCID, 4, 0),()),
		"LineHeight": ((112, LCID, 4, 0),()),
		"Position": ((12, LCID, 4, 0),()),
		"Selected": ((6, LCID, 4, 0),()),
		"Size": ((110, LCID, 4, 0),()),
		"Styles": ((102, LCID, 4, 0),()),
		"Text": ((101, LCID, 4, 0),()),
		"Visible": ((7, LCID, 4, 0),()),
		"WarningsIgnored": ((10, LCID, 4, 0),()),
		"WrapWidth": ((104, LCID, 4, 0),()),
		"index": ((8, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawTextStyle(DispatchBaseClass):
	'ChemDraw text style interface'
	CLSID = IID('{12A5FA9C-5C27-4006-9F31-0B91278D7F70}')
	coclass_clsid = IID('{7F97C7DD-07E9-45D8-9B6D-EAC2C094336F}')

	_prop_map_get_ = {
		"Color": (5, 2, (19, 0), (), "Color", None),
		"Face": (4, 2, (3, 0), (), "Face", None),
		"Family": (2, 2, (8, 0), (), "Family", None),
		"Size": (3, 2, (5, 0), (), "Size", None),
		"StartChar": (1, 2, (3, 0), (), "StartChar", None),
	}
	_prop_map_put_ = {
		"Color": ((5, LCID, 4, 0),()),
		"Face": ((4, LCID, 4, 0),()),
		"Family": ((2, LCID, 4, 0),()),
		"Size": ((3, LCID, 4, 0),()),
		"StartChar": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemDrawTextStyles(DispatchBaseClass):
	'ChemDraw text styles interface'
	CLSID = IID('{B27DB485-6C90-45D2-82C1-7D2F55D73654}')
	coclass_clsid = IID('{70CE4755-9513-4C41-B4FB-CD7FADFABEC5}')

	# Result is of type IChemDrawTextStyle
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{12A5FA9C-5C27-4006-9F31-0B91278D7F70}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{12A5FA9C-5C27-4006-9F31-0B91278D7F70}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{12A5FA9C-5C27-4006-9F31-0B91278D7F70}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemDrawTexts(DispatchBaseClass):
	'ChemDraw captions interface'
	CLSID = IID('{D156092E-1412-458C-BD6A-3CC171B56E63}')
	coclass_clsid = IID('{08D68E3F-E1CB-4E6A-B7D8-8D27D4D0FF43}')

	# Result is of type IChemDrawText
	def Item(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (3, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		'Given an index, returns an object in the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemOfficeMenu(DispatchBaseClass):
	'IChemOfficeMenu interface'
	CLSID = IID('{86BE5C06-1B92-11D0-87CF-1020AFD1F1AF}')
	coclass_clsid = IID('{52E62199-79D7-4279-8F36-CAAB57814C00}')

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Enabled": (3, 2, (11, 0), (), "Enabled", None),
		"MenuItems": (5, 2, (9, 0), (), "MenuItems", None),
		"Parent": (6, 2, (9, 0), (), "Parent", None),
		"caption": (2, 2, (8, 0), (), "caption", None),
		"index": (4, 2, (2, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Enabled": ((3, LCID, 4, 0),()),
		"caption": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemOfficeMenuBar(DispatchBaseClass):
	'IChemOfficeMenuBar interface'
	CLSID = IID('{86BE5C02-1B92-11D0-87CF-1020AFD1F1AF}')
	coclass_clsid = IID('{02C35511-5742-4351-AB70-C3B08FFFB38A}')

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Menus": (3, 2, (9, 0), (), "Menus", None),
		"Parent": (4, 2, (9, 0), (), "Parent", None),
		"index": (2, 2, (2, 0), (), "index", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemOfficeMenuBars(DispatchBaseClass):
	'IChemOfficeMenuBars interface'
	CLSID = IID('{86BE5C00-1B92-11D0-87CF-1020AFD1F1AF}')
	coclass_clsid = IID('{32488EE6-8194-4A7D-98DC-8F8B9E48293B}')

	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((2, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (2, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((2, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemOfficeMenuItem(DispatchBaseClass):
	CLSID = IID('{86BE5C0A-1B92-11D0-87CF-1020AFD1F1AF}')
	coclass_clsid = IID('{23F9462B-E682-4B4F-82A1-7BFF7B682B0E}')

	def Execute(self):
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Checked": (3, 2, (11, 0), (), "Checked", None),
		"CommandID": (7, 2, (2, 0), (), "CommandID", None),
		"Enabled": (4, 2, (11, 0), (), "Enabled", None),
		"Parent": (6, 2, (9, 0), (), "Parent", None),
		"caption": (2, 2, (8, 0), (), "caption", None),
		"index": (5, 2, (2, 0), (), "index", None),
	}
	_prop_map_put_ = {
		"Checked": ((3, LCID, 4, 0),()),
		"Enabled": ((4, LCID, 4, 0),()),
		"caption": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChemOfficeMenuItems(DispatchBaseClass):
	'IChemOfficeMenuItems interface'
	CLSID = IID('{86BE5C08-1B92-11D0-87CF-1020AFD1F1AF}')
	coclass_clsid = IID('{2F749F8C-CAC3-4E31-9877-A311AB601053}')

	def Add(self, caption=defaultNamedNotOptArg, beforeIndex=defaultNamedNotOptArg, objectName=defaultNamedOptArg, itemType=defaultNamedOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((8, 1), (16396, 1), (16396, 17), (16396, 17)),caption
			, beforeIndex, objectName, itemType)
		if ret is not None:
			ret = Dispatch(ret, 'Add', None)
		return ret

	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	def Remove(self, index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((16396, 1),),index
			)

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (2, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

class IChemOfficeMenus(DispatchBaseClass):
	'IChemOfficeMenus interface'
	CLSID = IID('{86BE5C04-1B92-11D0-87CF-1020AFD1F1AF}')
	coclass_clsid = IID('{65109431-873E-4933-9C0C-3F98374EE919}')

	def Add(self, caption=defaultNamedNotOptArg, beforeIndex=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((8, 1), (16396, 1)),caption
			, beforeIndex)
		if ret is not None:
			ret = Dispatch(ret, 'Add', None)
		return ret

	def Item(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	def Remove(self, index=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((16396, 1),),index
			)

	_prop_map_get_ = {
		"Application": (1, 2, (9, 0), (), "Application", None),
		"Count": (2, 2, (2, 0), (), "Count", None),
		"Parent": (3, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, index=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((16396, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(2, 2, (2, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __bool__(self):
		return True

from win32com.client import CoClassBaseClass
class AltGroup(CoClassBaseClass): # A CoClass
	# ChemDraw Alternative Group Class
	CLSID = IID('{3CA7EAEC-2ED5-4E60-8261-D60CAA24F975}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawAltGroup,
		IChemDrawObject,
	]
	default_interface = IChemDrawAltGroup

class AltGroups(CoClassBaseClass): # A CoClass
	# ChemDraw Alternative Groups Class
	CLSID = IID('{823B2C7E-8DC5-49BF-9FF1-F24F32A0B7AB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawAltGroups,
	]
	default_interface = IChemDrawAltGroups

class Annotation(CoClassBaseClass): # A CoClass
	# ChemDraw Annotation Class
	CLSID = IID('{DC1684DE-6A24-43AD-900C-BCE5150BB1F6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawAnnotation,
	]
	default_interface = IChemDrawAnnotation

class Annotations(CoClassBaseClass): # A CoClass
	# ChemDraw Annotations Class
	CLSID = IID('{AABDCC57-9D7B-4C81-9390-5703015A09E3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawAnnotations,
	]
	default_interface = IChemDrawAnnotations

# This CoClass is known by the name 'ChemDraw_x64.Application'
class Application(CoClassBaseClass): # A CoClass
	# ChemDraw Application Class
	CLSID = IID('{C172F840-938F-4A55-A732-4A036E3FBF3D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawApplication,
	]
	default_interface = IChemDrawApplication

class Arrow(CoClassBaseClass): # A CoClass
	# ChemDraw Arrow Class
	CLSID = IID('{0902D2BB-C8B3-4301-BE9C-D19443534718}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawArrow,
		IChemDrawObject,
	]
	default_interface = IChemDrawArrow

class Arrows(CoClassBaseClass): # A CoClass
	# ChemDraw Arrows Class
	CLSID = IID('{54B822AD-CD66-452E-A985-F7A78AD09987}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawArrows,
	]
	default_interface = IChemDrawArrows

class Atom(CoClassBaseClass): # A CoClass
	# ChemDraw Atom Class
	CLSID = IID('{2529F00D-9844-4F38-BDEB-6F59CFB816D7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawAtom,
		IChemDrawObject,
	]
	default_interface = IChemDrawAtom

class Atoms(CoClassBaseClass): # A CoClass
	# ChemDraw Atoms Class
	CLSID = IID('{D8276FFA-D137-4E55-9A86-5E73A3407617}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawAtoms,
	]
	default_interface = IChemDrawAtoms

class Bond(CoClassBaseClass): # A CoClass
	# ChemDraw Bond Class
	CLSID = IID('{5A4404EB-85A0-46D1-9157-97796E11133E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawBond,
		IChemDrawObject,
	]
	default_interface = IChemDrawBond

class Bonds(CoClassBaseClass): # A CoClass
	# ChemDraw Bonds Class
	CLSID = IID('{ED49B2DA-B782-4C80-B10A-6929EF115652}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawBonds,
	]
	default_interface = IChemDrawBonds

class Border(CoClassBaseClass): # A CoClass
	# ChemDraw Border Class
	CLSID = IID('{C7B5B8A1-F00F-4DDB-8DB9-C424E3342CF0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawBorder,
	]
	default_interface = IChemDrawBorder

class Bracket(CoClassBaseClass): # A CoClass
	# ChemDraw Bracket Class
	CLSID = IID('{5F717BE1-0415-4397-A493-F61E9315356D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawBracket,
		IChemDrawObject,
	]
	default_interface = IChemDrawBracket

class Brackets(CoClassBaseClass): # A CoClass
	# ChemDraw Brackets Class
	CLSID = IID('{CC11162C-C954-4859-A9C4-37B6C06C3F4B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawBrackets,
	]
	default_interface = IChemDrawBrackets

class Captions(CoClassBaseClass): # A CoClass
	# ChemDraw Captions Class
	CLSID = IID('{08D68E3F-E1CB-4E6A-B7D8-8D27D4D0FF43}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTexts,
	]
	default_interface = IChemDrawTexts

class Cell(CoClassBaseClass): # A CoClass
	# ChemDraw Cell Class
	CLSID = IID('{4ABDA8EB-29B0-469D-B937-F213AA330CEC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawCell,
	]
	default_interface = IChemDrawCell

class Cells(CoClassBaseClass): # A CoClass
	# ChemDraw Cells Class
	CLSID = IID('{504B85C3-4DA8-4C83-9C1D-C34C447491C7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawCells,
	]
	default_interface = IChemDrawCells

class Constraint(CoClassBaseClass): # A CoClass
	# ChemDraw Constraint Class
	CLSID = IID('{59D52749-0AE5-4AE5-A5BE-7534DA8DD900}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawConstraint,
		IChemDrawObject,
	]
	default_interface = IChemDrawConstraint

class Constraints(CoClassBaseClass): # A CoClass
	# ChemDraw Constraints Class
	CLSID = IID('{A7E7C374-E261-414A-847C-ED92818617F9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawConstraints,
	]
	default_interface = IChemDrawConstraints

class DataTypes(CoClassBaseClass): # A CoClass
	# CS ChemDraw 64-bit Data Type List Class
	CLSID = IID('{B8DAB55C-E0EC-4337-B1F0-D8ECABD6955F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawDataTypes,
	]
	default_interface = IChemDrawDataTypes

# This CoClass is known by the name 'ChemDraw_x64.Document.6.0'
class DocumentWin(CoClassBaseClass): # A CoClass
	# ChemDraw Document Class
	CLSID = IID('{41BA6D21-A02E-11CE-8FD9-0020AFD1F20C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawDocument,
	]
	default_interface = IChemDrawDocument

class Documents(CoClassBaseClass): # A CoClass
	# ChemDraw Document Collection Class
	CLSID = IID('{EFD13774-5475-4FE1-A9BC-32FACFC0FEF2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawDocuments,
	]
	default_interface = IChemDrawDocuments

class FragmentationAnalyzer(CoClassBaseClass): # A CoClass
	# ChemDraw Fragmentation Event Class
	CLSID = IID('{D716300D-8CBF-40FF-9C58-9CCEA0F34DDD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawFragmentationAnalyzer,
		IChemDrawObject,
	]
	default_interface = IChemDrawFragmentationAnalyzer

class FragmentationLine(CoClassBaseClass): # A CoClass
	# ChemDraw Fragmentation Line Class
	CLSID = IID('{D716300D-8CBF-40FF-9C58-9CCEA0F3EFFF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawFragmentationLine,
		IChemDrawObject,
	]
	default_interface = IChemDrawFragmentationLine

class FragmentationLines(CoClassBaseClass): # A CoClass
	# ChemDraw Fragmentation Lines Class
	CLSID = IID('{7D717A46-968E-47EB-B78E-C32DD437EFFF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawFragmentationLines,
	]
	default_interface = IChemDrawFragmentationLines

class Geometries(CoClassBaseClass): # A CoClass
	# ChemDraw Geometries Class
	CLSID = IID('{3DA3006C-EA2E-4E6C-A9C0-163A5774A3EF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawGeometries,
	]
	default_interface = IChemDrawGeometries

class Geometry(CoClassBaseClass): # A CoClass
	# ChemDraw Geometry Class
	CLSID = IID('{425C0C02-0AC8-48F4-A0F7-E6E7A61EDB2A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawGeometry,
		IChemDrawObject,
	]
	default_interface = IChemDrawGeometry

class Graphic(CoClassBaseClass): # A CoClass
	# ChemDraw Graphic Object Class
	CLSID = IID('{637AB4EC-B34C-4708-B06A-E8E5922302AA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawGraphic,
		IChemDrawObject,
	]
	default_interface = IChemDrawGraphic

class Graphics(CoClassBaseClass): # A CoClass
	# ChemDraw Graphic Objects Class
	CLSID = IID('{05B8BA9A-2869-44AD-A3FB-A8D6F392F6FC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawGraphics,
	]
	default_interface = IChemDrawGraphics

class Group(CoClassBaseClass): # A CoClass
	# ChemDraw Group Class
	CLSID = IID('{1C41DA07-5244-447F-AD57-43DCD32F88A5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawGroup,
		IChemDrawObject,
	]
	default_interface = IChemDrawGroup

class Groups(CoClassBaseClass): # A CoClass
	# ChemDraw Groups Class
	CLSID = IID('{47CF6326-FBAF-49C9-BA9C-F6242EB52DC6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawGroups,
	]
	default_interface = IChemDrawGroups

class MassFragment(CoClassBaseClass): # A CoClass
	# ChemDraw Mass Fragment Class
	CLSID = IID('{D716300D-8CBF-40FF-9C58-9CCEA0F34FFF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawMassFragment,
		IChemDrawObject,
	]
	default_interface = IChemDrawMassFragment

class MassFragments(CoClassBaseClass): # A CoClass
	# ChemDraw Mass Fragments Class
	CLSID = IID('{7D717A46-968E-47EB-B78E-C32DD437DFFF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawMassFragments,
	]
	default_interface = IChemDrawMassFragments

class Menu(CoClassBaseClass): # A CoClass
	# Menu object
	CLSID = IID('{52E62199-79D7-4279-8F36-CAAB57814C00}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemOfficeMenu,
	]
	default_interface = IChemOfficeMenu

class MenuBar(CoClassBaseClass): # A CoClass
	# MenuBar object
	CLSID = IID('{02C35511-5742-4351-AB70-C3B08FFFB38A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemOfficeMenuBar,
	]
	default_interface = IChemOfficeMenuBar

class MenuBars(CoClassBaseClass): # A CoClass
	# MenuBars collection
	CLSID = IID('{32488EE6-8194-4A7D-98DC-8F8B9E48293B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemOfficeMenuBars,
	]
	default_interface = IChemOfficeMenuBars

class MenuItem(CoClassBaseClass): # A CoClass
	# MenuItem object
	CLSID = IID('{23F9462B-E682-4B4F-82A1-7BFF7B682B0E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemOfficeMenuItem,
	]
	default_interface = IChemOfficeMenuItem

class MenuItems(CoClassBaseClass): # A CoClass
	# MenuItems collection
	CLSID = IID('{2F749F8C-CAC3-4E31-9877-A311AB601053}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemOfficeMenuItems,
	]
	default_interface = IChemOfficeMenuItems

class Menus(CoClassBaseClass): # A CoClass
	# Menus collection
	CLSID = IID('{65109431-873E-4933-9C0C-3F98374EE919}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemOfficeMenus,
	]
	default_interface = IChemOfficeMenus

class Object(CoClassBaseClass): # A CoClass
	# ChemDraw Object Class
	CLSID = IID('{200850C1-6797-4C1D-960D-7917936531EE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawObject,
	]
	default_interface = IChemDrawObject

class ObjectTag(CoClassBaseClass): # A CoClass
	# ChemDraw Object Tag Class
	CLSID = IID('{A6011FEC-EF26-417A-9E0F-DF9379873DAF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawObjectTag,
		IChemDrawObject,
	]
	default_interface = IChemDrawObjectTag

class ObjectTags(CoClassBaseClass): # A CoClass
	# ChemDraw Object Tags Class
	CLSID = IID('{F5F5A846-177D-4987-8D57-B3A401618C04}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawObjectTags,
	]
	default_interface = IChemDrawObjectTags

class Objects(CoClassBaseClass): # A CoClass
	# ChemDraw Object Collection Class
	CLSID = IID('{75DC8A59-DF79-481D-82F6-0BA538978791}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawObjects,
	]
	default_interface = IChemDrawObjects

class Picture(CoClassBaseClass): # A CoClass
	# ChemDraw Picture Class
	CLSID = IID('{46CB2881-7626-4C35-A4D7-45F245CC8376}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPicture,
		IChemDrawObject,
	]
	default_interface = IChemDrawPicture

class Pictures(CoClassBaseClass): # A CoClass
	# ChemDraw Pictures Class
	CLSID = IID('{24535E40-072D-4068-AA42-154513415BB3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPictures,
	]
	default_interface = IChemDrawPictures

class PlasmidMap(CoClassBaseClass): # A CoClass
	# ChemDraw Plasmid Map Class
	CLSID = IID('{4B87F2A6-B4BD-4418-9610-0216BC7DC190}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPlasmidMap,
		IChemDrawObject,
	]
	default_interface = IChemDrawPlasmidMap

class PlasmidMaps(CoClassBaseClass): # A CoClass
	# ChemDraw PlasmidMaps Class
	CLSID = IID('{E2CB8432-6642-4DEB-B956-A6A579922E80}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPlasmidMaps,
	]
	default_interface = IChemDrawPlasmidMaps

class PlasmidMarker(CoClassBaseClass): # A CoClass
	# ChemDraw Plasmid Marker Class
	CLSID = IID('{DA5D0F99-162A-45B0-B81B-0F48A4781DE2}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPlasmidMarker,
		IChemDrawObjectTag,
	]
	default_interface = IChemDrawPlasmidMarker

class PlasmidMarkers(CoClassBaseClass): # A CoClass
	# ChemDraw PlasmidMarkers Class
	CLSID = IID('{10840A43-1023-47A4-AD33-3C92B257DD61}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPlasmidMarkers,
	]
	default_interface = IChemDrawPlasmidMarkers

class PlasmidRegion(CoClassBaseClass): # A CoClass
	# ChemDraw Plasmid Region Class
	CLSID = IID('{E0D25ABD-8210-4390-AF26-EC7B85C651FA}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPlasmidRegion,
		IChemDrawArrow,
	]
	default_interface = IChemDrawPlasmidRegion

class PlasmidRegions(CoClassBaseClass): # A CoClass
	# ChemDraw PlasmidRegions Class
	CLSID = IID('{2193B148-381B-486E-B96B-B21C6CD6AD02}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPlasmidRegions,
	]
	default_interface = IChemDrawPlasmidRegions

class Point(CoClassBaseClass): # A CoClass
	# ChemDraw Point Class
	CLSID = IID('{A61082F6-DD43-4DF4-9B7C-C25B0024DB4D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPoint,
	]
	default_interface = IChemDrawPoint

class Preferences(CoClassBaseClass): # A CoClass
	# ChemDraw Preferences Class
	CLSID = IID('{7C97009F-5782-4C5B-8601-7784BDE3F73D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawPreferences,
	]
	default_interface = IChemDrawPreferences

class ReactionScheme(CoClassBaseClass): # A CoClass
	# ChemDraw Reaction Scheme Class
	CLSID = IID('{8BC99E8A-2E32-449B-A22F-BFBE43903E91}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawReactionScheme,
		IChemDrawObject,
	]
	default_interface = IChemDrawReactionScheme

class ReactionSchemes(CoClassBaseClass): # A CoClass
	# ChemDraw Reaction Schemes Class
	CLSID = IID('{C1782781-382B-4D8F-84F7-D94AD34299FC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawReactionSchemes,
	]
	default_interface = IChemDrawReactionSchemes

class ReactionStep(CoClassBaseClass): # A CoClass
	# ChemDraw Reaction Step Class
	CLSID = IID('{125A7E5F-B055-45E0-894E-BFB0405809F7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawReactionStep,
		IChemDrawObject,
	]
	default_interface = IChemDrawReactionStep

class ReactionStepComponents(CoClassBaseClass): # A CoClass
	# ChemDraw Reaction Step Components Class
	CLSID = IID('{9A7B95B6-AA5B-4CC7-B996-D99989051F60}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawReactionStepComponents,
	]
	default_interface = IChemDrawReactionStepComponents

class ReactionSteps(CoClassBaseClass): # A CoClass
	# ChemDraw Reaction Steps Class
	CLSID = IID('{9F8EDE4B-1872-4ABE-9255-1F3A49703F3E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawReactionSteps,
	]
	default_interface = IChemDrawReactionSteps

class Rect(CoClassBaseClass): # A CoClass
	# ChemDraw Rectangle Class
	CLSID = IID('{3A0F4F2C-92C7-4569-96B6-D608BCBAFD66}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawRect,
	]
	default_interface = IChemDrawRect

class SGComponent(CoClassBaseClass): # A CoClass
	# ChemDraw Stoichiometry Grid Component Class
	CLSID = IID('{22144C17-01EC-471D-B15E-C40090786B54}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSGComponent,
	]
	default_interface = IChemDrawSGComponent

class SGComponents(CoClassBaseClass): # A CoClass
	# ChemDraw Stoichiometry Grid Components Class
	CLSID = IID('{BE1FFDC2-A4B8-4B8E-99C9-9AB476904B5F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSGComponents,
	]
	default_interface = IChemDrawSGComponents

class SGProperties(CoClassBaseClass): # A CoClass
	# ChemDraw Stoichiometry Grid Properties Class
	CLSID = IID('{181B972B-956D-4A92-BEDE-6B81D3232694}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSGProperties,
	]
	default_interface = IChemDrawSGProperties

class SGProperty(CoClassBaseClass): # A CoClass
	# ChemDraw Stoichiometry Grid Property Class
	CLSID = IID('{D41B5DF8-89D0-4D7B-9811-F510AECB6798}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSGProperty,
	]
	default_interface = IChemDrawSGProperty

class Selection(CoClassBaseClass): # A CoClass
	# ChemDraw Selection Class
	CLSID = IID('{7AF6DD12-F154-4FAE-8437-3B51CD00A5DE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSelection,
	]
	default_interface = IChemDrawSelection

class Settings(CoClassBaseClass): # A CoClass
	# ChemDraw Settings Class
	CLSID = IID('{290E5D0A-000C-405D-8E83-895CC9E3D8C4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSettings,
	]
	default_interface = IChemDrawSettings

class Spline(CoClassBaseClass): # A CoClass
	# ChemDraw Spline Class
	CLSID = IID('{FEDAEFD6-F32A-40A8-97D5-8E5DF32425B3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSpline,
		IChemDrawObject,
	]
	default_interface = IChemDrawSpline

class Splines(CoClassBaseClass): # A CoClass
	# ChemDraw Splines Class
	CLSID = IID('{31D1265E-BF76-43FE-A7B0-257325B904B3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSplines,
	]
	default_interface = IChemDrawSplines

class StoichiometryGrid(CoClassBaseClass): # A CoClass
	# ChemDraw Stoichiometry Grid Class
	CLSID = IID('{1018F877-126F-44EB-8C26-D3A3E5286956}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawStoichiometryGrid,
		IChemDrawObject,
	]
	default_interface = IChemDrawStoichiometryGrid

class StoichiometryGrids(CoClassBaseClass): # A CoClass
	# ChemDraw Stoichiometry Grids Class
	CLSID = IID('{F51EC5B2-1756-455F-9F1F-59188D877D20}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawStoichiometryGrids,
	]
	default_interface = IChemDrawStoichiometryGrids

class Style(CoClassBaseClass): # A CoClass
	# ChemDraw Text Style Class
	CLSID = IID('{7F97C7DD-07E9-45D8-9B6D-EAC2C094336F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTextStyle,
	]
	default_interface = IChemDrawTextStyle

class Styles(CoClassBaseClass): # A CoClass
	# ChemDraw Text Styles Class
	CLSID = IID('{70CE4755-9513-4C41-B4FB-CD7FADFABEC5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTextStyles,
	]
	default_interface = IChemDrawTextStyles

class Symbol(CoClassBaseClass): # A CoClass
	# ChemDraw Symbol Class
	CLSID = IID('{2984EE75-82FC-46B2-AE1E-8A82C77F2DE1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSymbol,
		IChemDrawObject,
	]
	default_interface = IChemDrawSymbol

class Symbols(CoClassBaseClass): # A CoClass
	# ChemDraw Symbols Class
	CLSID = IID('{2470A7A4-3845-4AE3-8034-82F091367BF4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawSymbols,
	]
	default_interface = IChemDrawSymbols

class TLCLane(CoClassBaseClass): # A CoClass
	# ChemDraw TLC Lane Class
	CLSID = IID('{22B44C17-01EC-471D-B15E-C40090786B54}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTLCLane,
	]
	default_interface = IChemDrawTLCLane

class TLCLanes(CoClassBaseClass): # A CoClass
	# ChemDraw TLC Lanes Class
	CLSID = IID('{BE7FFDC2-A4B8-4B8E-99C9-9AB476904B5F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTLCLanes,
	]
	default_interface = IChemDrawTLCLanes

class TLCPlate(CoClassBaseClass): # A CoClass
	# ChemDraw TLC Plate Class
	CLSID = IID('{1098F877-126F-44EB-8C26-D3A3E5286956}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTLCPlate,
		IChemDrawObject,
	]
	default_interface = IChemDrawTLCPlate

class TLCPlates(CoClassBaseClass): # A CoClass
	# ChemDraw TLC Plates Class
	CLSID = IID('{F5EEC5B2-1756-455F-9F1F-59188D877D20}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTLCPlates,
	]
	default_interface = IChemDrawTLCPlates

class TLCSpot(CoClassBaseClass): # A CoClass
	# ChemDraw TLC Spot Class
	CLSID = IID('{D43B5DF8-89D0-4D7B-9811-F510AECB6798}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTLCSpot,
	]
	default_interface = IChemDrawTLCSpot

class TLCSpots(CoClassBaseClass): # A CoClass
	# ChemDraw TLC Spots Class
	CLSID = IID('{188B972B-956D-4A92-BEDE-6B81D3232694}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTLCSpots,
	]
	default_interface = IChemDrawTLCSpots

class Table(CoClassBaseClass): # A CoClass
	# ChemDraw Table Class
	CLSID = IID('{A803FB2E-9C62-4E72-8742-418C8892B15F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTable,
		IChemDrawObject,
	]
	default_interface = IChemDrawTable

class Tables(CoClassBaseClass): # A CoClass
	# ChemDraw Tables Class
	CLSID = IID('{DA47E69C-6A9A-4C52-8754-0158EC317F39}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawTables,
	]
	default_interface = IChemDrawTables

class caption(CoClassBaseClass): # A CoClass
	# ChemDraw Caption Class
	CLSID = IID('{9B1B67CB-9794-4432-8F2D-766ED39AB5C4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawText,
		IChemDrawObject,
	]
	default_interface = IChemDrawText

class dataType(CoClassBaseClass): # A CoClass
	# CS ChemDraw 64-bit Data Type Class
	CLSID = IID('{1E1AC724-C06D-4078-9E42-DBB291BA236B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChemDrawDataType,
	]
	default_interface = IChemDrawDataType

DataObject_vtables_dispatch_ = 1
DataObject_vtables_ = [
	(( 'Clear' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetData' , 'Value' , 'Format' , ), 2, (2, (), [ (12, 17, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 2 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetData' , 'Format' , 'retval' , ), 3, (3, (), [ (3, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetFormat' , 'Format' , 'retval' , ), 4, (4, (), [ (3, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Files' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{41A7D761-6018-11CF-9016-00AA0068841E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

DataObjectFiles_vtables_dispatch_ = 1
DataObjectFiles_vtables_ = [
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'Return' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Filename' , 'index' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (12, 17, None, None) , ], 1 , 1 , 4 , 1 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 3, (3, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'index' , ), 4, (4, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'Return' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IChemDrawAltGroup_vtables_dispatch_ = 1
IChemDrawAltGroup_vtables_ = [
	(( 'Objects' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'caption' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TextFrame' , 'pVal' , ), 103, (103, (), [ (16393, 10, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'TextFrame' , 'pVal' , ), 103, (103, (), [ (9, 1, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GroupFrame' , 'pVal' , ), 104, (104, (), [ (16393, 10, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'GroupFrame' , 'pVal' , ), 104, (104, (), [ (9, 1, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Atoms' , 'retval' , ), 301, (301, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Bonds' , 'retval' , ), 302, (302, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Graphics' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{D0E3D4B9-3B16-4331-BBA2-651319AE0402}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Splines' , 'retval' , ), 304, (304, (), [ (16393, 10, None, "IID('{272423F1-2909-4340-8870-8062530ADD05}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Captions' , 'retval' , ), 305, (305, (), [ (16393, 10, None, "IID('{D156092E-1412-458C-BD6A-3CC171B56E63}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Pictures' , 'retval' , ), 306, (306, (), [ (16393, 10, None, "IID('{41652842-15D6-44AE-AEFF-B51B179CF019}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Groups' , 'retval' , ), 307, (307, (), [ (16393, 10, None, "IID('{E5164832-7AFC-463A-9C19-A1AF6D191020}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Tables' , 'retval' , ), 308, (308, (), [ (16393, 10, None, "IID('{80C78566-D4BF-460E-B055-5728877FB30E}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'AltGroups' , 'retval' , ), 309, (309, (), [ (16393, 10, None, "IID('{D9E5D3D1-0D59-4126-B108-7D567E396FB3}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Geometries' , 'retval' , ), 310, (310, (), [ (16393, 10, None, "IID('{53C77081-53BF-4397-9BB4-84D6AF7C10F3}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'retval' , ), 311, (311, (), [ (16393, 10, None, "IID('{990C82BE-55F2-49F2-B822-2E448C7FEC80}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ReactionSchemes' , 'retval' , ), 312, (312, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'TLCPlates' , 'retval' , ), 313, (313, (), [ (16393, 10, None, "IID('{27609627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'StoichiometryGrids' , 'retval' , ), 314, (314, (), [ (16393, 10, None, "IID('{27109627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'PlasmidMaps' , 'retval' , ), 315, (315, (), [ (16393, 10, None, "IID('{E06B3507-3060-4095-8406-BAADD00A054E}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Arrows' , 'retval' , ), 316, (316, (), [ (16393, 10, None, "IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'retval' , ), 319, (319, (), [ (16393, 10, None, "IID('{D44C587D-2434-46B8-8B76-D309A2632456}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Brackets' , 'retval' , ), 320, (320, (), [ (16393, 10, None, "IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IChemDrawAltGroups_vtables_dispatch_ = 1
IChemDrawAltGroups_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawAnnotation_vtables_dispatch_ = 1
IChemDrawAnnotation_vtables_ = [
	(( 'Keyword' , 'pVal' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Content' , 'pVal' , ), 102, (102, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Content' , 'pVal' , ), 102, (102, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IChemDrawAnnotations_vtables_dispatch_ = 1
IChemDrawAnnotations_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{DBD6A772-8979-4049-A58A-AA8F5D56A779}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'Keyword' , 'Content' , ), 1610743813, (1610743813, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'Keyword' , ), 1610743814, (1610743814, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetAnnotation' , 'Keyword' , 'retval' , ), 1610743815, (1610743815, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{DBD6A772-8979-4049-A58A-AA8F5D56A779}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IChemDrawApplication_vtables_dispatch_ = 1
IChemDrawApplication_vtables_ = [
	(( 'name' , 'retval' , ), 0, (0, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ActiveDocument' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{9E3A4685-0A8F-420D-A73E-4A37B83830DB}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Documents' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'retval' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'retval' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'MenuBars' , 'retval' , ), 7, (7, (), [ (16393, 10, None, "IID('{86BE5C00-1B92-11D0-87CF-1020AFD1F1AF}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Preferences' , 'pVal' , ), 8, (8, (), [ (16393, 10, None, "IID('{4BC8155A-553E-4992-A555-FEEECB11CAB8}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MainWindow' , 'retval' , ), 9, (9, (), [ (16404, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DefaultDataType' , 'pVal' , ), 11, (11, (), [ (16393, 10, None, "IID('{BB42A8EF-A444-40C2-BF4F-E156341E4127}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DefaultDataType' , 'pVal' , ), 11, (11, (), [ (9, 1, None, "IID('{BB42A8EF-A444-40C2-BF4F-E156341E4127}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ImportDataTypes' , 'pVal' , ), 12, (12, (), [ (16393, 10, None, "IID('{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ExportDataTypes' , 'pVal' , ), 13, (13, (), [ (16393, 10, None, "IID('{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'IODataTypes' , 'pVal' , ), 14, (14, (), [ (16393, 10, None, "IID('{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Quit' , ), 1610743820, (1610743820, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateRunLevel' , 'progLevel' , ), 15, (15, (), [ (12, 0, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IChemDrawArrow_vtables_dispatch_ = 1
IChemDrawArrow_vtables_ = [
	(( 'Start' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Start' , 'pVal' , ), 101, (101, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'End' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'End' , 'pVal' , ), 102, (102, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'LineType' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'LineType' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadType' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadType' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionStart' , 'pVal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionStart' , 'pVal' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionTail' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionTail' , 'pVal' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'IsArc' , 'pVal' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'IsStraightArrow' , 'pVal' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'IsLine' , 'pVal' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'IsBold' , 'pVal' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'IsBold' , 'pVal' , ), 110, (110, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'IsDashed' , 'pVal' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'IsDashed' , 'pVal' , ), 111, (111, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'HeadSize' , 'pVal' , ), 112, (112, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'HeadSize' , 'pVal' , ), 112, (112, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'AngularSize' , 'pVal' , ), 113, (113, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'AngularSize' , 'pVal' , ), 113, (113, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'HeadCenterSize' , 'pVal' , ), 114, (114, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'HeadCenterSize' , 'pVal' , ), 114, (114, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'HeadWidth' , 'pVal' , ), 115, (115, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'HeadWidth' , 'pVal' , ), 115, (115, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'ShaftSpacing' , 'pVal' , ), 116, (116, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'ShaftSpacing' , 'pVal' , ), 116, (116, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'EquilibriumRatio' , 'pVal' , ), 117, (117, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'EquilibriumRatio' , 'pVal' , ), 117, (117, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'IsWavy' , 'pVal' , ), 118, (118, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'IsWavy' , 'pVal' , ), 118, (118, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'IsNoGo' , 'pVal' , ), 119, (119, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'IsDipole' , 'pVal' , ), 120, (120, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'IsDipole' , 'pVal' , ), 120, (120, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'NoGoType' , 'pVal' , ), 121, (121, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'NoGoType' , 'pVal' , ), 121, (121, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'ArcOrigin' , 'pVal' , ), 122, (122, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'ArcOrigin' , 'pVal' , ), 122, (122, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
]

IChemDrawArrows_vtables_dispatch_ = 1
IChemDrawArrows_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{669C0868-90B0-4469-9621-7639880698B1}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawAtom_vtables_dispatch_ = 1
IChemDrawAtom_vtables_ = [
	(( 'NodeType' , 'pVal' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ElementNumber' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ElementNumber' , 'pVal' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Charge' , 'pVal' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Charge' , 'pVal' , ), 103, (103, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Radical' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Radical' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Isotope' , 'pVal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Isotope' , 'pVal' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'NumImplicitHydrogens' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'NumImplicitHydrogens' , 'pVal' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'LabelDisplay' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'LabelDisplay' , 'pVal' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'AttachedAtoms' , 'pVal' , ), 108, (108, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'AddAttachedAtom' , 'pVal' , ), 109, (109, (), [ (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAttachedAtom' , 'pVal' , ), 110, (110, (), [ (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'IsHDot' , 'pVal' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'IsHDot' , 'pVal' , ), 111, (111, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'IsHDash' , 'pVal' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'IsHDash' , 'pVal' , ), 112, (112, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Stereochemistry' , 'pVal' , ), 113, (113, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Stereochemistry' , 'pVal' , ), 113, (113, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'AtomNumber' , 'pVal' , ), 114, (114, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'AtomNumber' , 'pVal' , ), 114, (114, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'AtomGeometry' , 'pVal' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'SubstituentType' , 'pVal' , ), 116, (116, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'SubstituentType' , 'pVal' , ), 116, (116, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'SubstituentCount' , 'pVal' , ), 117, (117, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'SubstituentCount' , 'pVal' , ), 117, (117, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'RingBondCount' , 'pVal' , ), 118, (118, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'RingBondCount' , 'pVal' , ), 118, (118, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Unsaturation' , 'pVal' , ), 119, (119, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Unsaturation' , 'pVal' , ), 119, (119, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'ReactionStereo' , 'pVal' , ), 120, (120, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'ReactionStereo' , 'pVal' , ), 120, (120, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'Translation' , 'pVal' , ), 121, (121, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'Translation' , 'pVal' , ), 121, (121, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'IsotopicAbundance' , 'pVal' , ), 122, (122, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'IsotopicAbundance' , 'pVal' , ), 122, (122, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'ImplicitHydrogensAllowed' , 'pVal' , ), 123, (123, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'ImplicitHydrogensAllowed' , 'pVal' , ), 123, (123, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'AbnormalValenceAllowed' , 'pVal' , ), 124, (124, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'AbnormalValenceAllowed' , 'pVal' , ), 124, (124, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'RestrictReactionChange' , 'pVal' , ), 125, (125, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'RestrictReactionChange' , 'pVal' , ), 125, (125, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'LinkCountLow' , 'pVal' , ), 126, (126, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'LinkCountLow' , 'pVal' , ), 126, (126, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'LinkCountHigh' , 'pVal' , ), 127, (127, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'LinkCountHigh' , 'pVal' , ), 127, (127, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'AlternativeGroup' , 'pVal' , ), 128, (128, (), [ (16393, 10, None, "IID('{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')") , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'MappedAtoms' , 'pVal' , ), 129, (129, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'AddMappedAtom' , 'pVal' , ), 130, (130, (), [ (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 1 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'DeleteMapping' , ), 131, (131, (), [ ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'Bonds' , 'pVal' , ), 132, (132, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'UsedValences' , 'pVal' , ), 133, (133, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'UnusedValences' , 'pVal' , ), 134, (134, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'SBO' , 'pVal' , ), 135, (135, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'IsAttachmentPoint' , 'pVal' , ), 136, (136, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'IsAttachmentPoint' , 'pVal' , ), 136, (136, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'IsMultiCenter' , 'pVal' , ), 137, (137, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'IsMultiCenter' , 'pVal' , ), 137, (137, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'IsVariableAttach' , 'pVal' , ), 138, (138, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'IsVariableAttach' , 'pVal' , ), 138, (138, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'LabelText' , 'pVal' , ), 139, (139, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'LabelText' , 'pVal' , ), 139, (139, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'AttachmentPointType' , 'pVal' , ), 140, (140, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'AttachmentPointType' , 'pVal' , ), 140, (140, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'ExpandLabelToStructure' , ), 141, (141, (), [ ], 1 , 1 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'EnhancedStereoType' , 'pVal' , ), 142, (142, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'EnhancedStereoType' , 'pVal' , ), 142, (142, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'EnhancedStereoGroupNumber' , 'pVal' , ), 143, (143, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'EnhancedStereoGroupNumber' , 'pVal' , ), 143, (143, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
]

IChemDrawAtoms_vtables_dispatch_ = 1
IChemDrawAtoms_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawBond_vtables_dispatch_ = 1
IChemDrawBond_vtables_ = [
	(( 'Atom1' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Atom2' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'BondOrder' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'BondOrder' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'BondDisplay' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'BondDisplay' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'BondDisplay2' , 'pVal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'BondDisplay2' , 'pVal' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'BondDoublePosition' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'BondDoublePosition' , 'pVal' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'AttachChar1' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'AttachChar1' , 'pVal' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'AttachChar2' , 'pVal' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'AttachChar2' , 'pVal' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Topology' , 'pVal' , ), 109, (109, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Topology' , 'pVal' , ), 109, (109, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'ReactionParticipation' , 'pVal' , ), 110, (110, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ReactionParticipation' , 'pVal' , ), 110, (110, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Stereochemistry' , 'pVal' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Stereochemistry' , 'pVal' , ), 111, (111, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'CrossingBonds' , 'pVal' , ), 112, (112, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'OtherAtom' , 'thisAtom' , 'OtherAtom' , ), 113, (113, (), [ (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , 
			 (16393, 10, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
]

IChemDrawBonds_vtables_dispatch_ = 1
IChemDrawBonds_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawBorder_vtables_dispatch_ = 1
IChemDrawBorder_vtables_ = [
	(( 'IsDashed' , 'pVal' , ), 1, (1, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'IsDashed' , 'pVal' , ), 1, (1, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3, (3, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3, (3, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IChemDrawBracket_vtables_dispatch_ = 1
IChemDrawBracket_vtables_ = [
	(( 'Start' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Start' , 'pVal' , ), 101, (101, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'End' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'End' , 'pVal' , ), 102, (102, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'BracketType' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'BracketType' , 'pVal' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'BracketUsage' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'BracketUsage' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'PolymerRepeatPattern' , 'pVal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'PolymerRepeatPattern' , 'pVal' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'PolymerFlipType' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'PolymerFlipType' , 'pVal' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'BracketLipSize' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ComponentOrder' , 'pVal' , ), 108, (108, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'ComponentOrder' , 'pVal' , ), 108, (108, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'RepeatCount' , 'pVal' , ), 109, (109, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'RepeatCount' , 'pVal' , ), 109, (109, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'SRULabel' , 'pVal' , ), 110, (110, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'SRULabel' , 'pVal' , ), 110, (110, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'CrossingBonds' , 'pVal' , ), 111, (111, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'InsideAtoms' , 'pVal' , ), 112, (112, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'OutsideAtoms' , 'pVal' , ), 113, (113, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'ContainedAtoms' , 'pVal' , ), 114, (114, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'PairedBrackets' , 'pVal' , ), 115, (115, (), [ (16393, 10, None, "IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IChemDrawBrackets_vtables_dispatch_ = 1
IChemDrawBrackets_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawCell_vtables_dispatch_ = 1
IChemDrawCell_vtables_ = [
	(( 'Objects' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TopBorder' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{40553F42-5954-43F2-B154-188727D588E1}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LeftBorder' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{40553F42-5954-43F2-B154-188727D588E1}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BottomBorder' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{40553F42-5954-43F2-B154-188727D588E1}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RightBorder' , 'retval' , ), 5, (5, (), [ (16393, 10, None, "IID('{40553F42-5954-43F2-B154-188727D588E1}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Atoms' , 'retval' , ), 301, (301, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Bonds' , 'retval' , ), 302, (302, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Graphics' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{D0E3D4B9-3B16-4331-BBA2-651319AE0402}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Splines' , 'retval' , ), 304, (304, (), [ (16393, 10, None, "IID('{272423F1-2909-4340-8870-8062530ADD05}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Captions' , 'retval' , ), 305, (305, (), [ (16393, 10, None, "IID('{D156092E-1412-458C-BD6A-3CC171B56E63}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Pictures' , 'retval' , ), 306, (306, (), [ (16393, 10, None, "IID('{41652842-15D6-44AE-AEFF-B51B179CF019}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Groups' , 'retval' , ), 307, (307, (), [ (16393, 10, None, "IID('{E5164832-7AFC-463A-9C19-A1AF6D191020}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Tables' , 'retval' , ), 308, (308, (), [ (16393, 10, None, "IID('{80C78566-D4BF-460E-B055-5728877FB30E}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AltGroups' , 'retval' , ), 309, (309, (), [ (16393, 10, None, "IID('{D9E5D3D1-0D59-4126-B108-7D567E396FB3}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Geometries' , 'retval' , ), 310, (310, (), [ (16393, 10, None, "IID('{53C77081-53BF-4397-9BB4-84D6AF7C10F3}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'retval' , ), 311, (311, (), [ (16393, 10, None, "IID('{990C82BE-55F2-49F2-B822-2E448C7FEC80}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ReactionSchemes' , 'retval' , ), 312, (312, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TLCPlates' , 'retval' , ), 313, (313, (), [ (16393, 10, None, "IID('{27609627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'StoichiometryGrids' , 'retval' , ), 314, (314, (), [ (16393, 10, None, "IID('{27109627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PlasmidMaps' , 'retval' , ), 315, (315, (), [ (16393, 10, None, "IID('{E06B3507-3060-4095-8406-BAADD00A054E}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Arrows' , 'retval' , ), 316, (316, (), [ (16393, 10, None, "IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'retval' , ), 319, (319, (), [ (16393, 10, None, "IID('{D44C587D-2434-46B8-8B76-D309A2632456}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Brackets' , 'retval' , ), 320, (320, (), [ (16393, 10, None, "IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'MakeAtom' , 'pVal' , ), 401, (401, (), [ (16393, 10, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MakeBond' , 'at1' , 'at2' , 'pVal' , ), 402, (402, (), [ 
			 (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , (16393, 10, None, "IID('{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MakeSpline' , 'pVal' , ), 404, (404, (), [ (16393, 10, None, "IID('{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'MakeCaption' , 'pVal' , ), 405, (405, (), [ (16393, 10, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'MakeGroup' , 'pVal' , ), 407, (407, (), [ (16393, 10, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'MakeTable' , 'pVal' , ), 408, (408, (), [ (16393, 10, None, "IID('{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'MakeAltGroup' , 'pVal' , ), 409, (409, (), [ (16393, 10, None, "IID('{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'MakeGeometry' , 'geomType' , 'pVal' , ), 410, (410, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{A9173267-C525-4660-93A0-C5FF4BC55057}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'MakeConstraint' , 'ConstraintType' , 'pVal' , ), 411, (411, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'MakeTLCPlate' , 'pVal' , ), 413, (413, (), [ (16393, 10, None, "IID('{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'MakeArrow' , 'pVal' , ), 414, (414, (), [ (16393, 10, None, "IID('{669C0868-90B0-4469-9621-7639880698B1}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'MakeBracket' , 'type' , 'pVal' , ), 415, (415, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'MakeSymbol' , 'type' , 'pVal' , ), 416, (416, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{0C9366BF-36BB-4303-86FA-966657FF891D}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'MakeRectangle' , 'pVal' , ), 417, (417, (), [ (16393, 10, None, "IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')") , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'MakeEllipse' , 'pVal' , ), 418, (418, (), [ (16393, 10, None, "IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')") , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'MakeOrbital' , 'type' , 'pVal' , ), 419, (419, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')") , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'MakeStoichiometryGrid' , 'pVal' , ), 420, (420, (), [ (16393, 10, None, "IID('{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'MakePlasmidMap' , 'pVal' , ), 421, (421, (), [ (16393, 10, None, "IID('{F06B3507-3060-4095-8406-CBBDD00A054E}')") , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

IChemDrawCells_vtables_dispatch_ = 1
IChemDrawCells_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawConstraint_vtables_dispatch_ = 1
IChemDrawConstraint_vtables_ = [
	(( 'BasisObjects' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintType' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'MinRange' , 'pVal' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'MinRange' , 'pVal' , ), 103, (103, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'MaxRange' , 'pVal' , ), 104, (104, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'MaxRange' , 'pVal' , ), 104, (104, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

IChemDrawConstraints_vtables_dispatch_ = 1
IChemDrawConstraints_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawDataType_vtables_dispatch_ = 1
IChemDrawDataType_vtables_ = [
	(( 'MIME' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Extension' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Valid' , 'pVal' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IChemDrawDataTypes_vtables_dispatch_ = 1
IChemDrawDataTypes_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Item' , 'index' , 'pVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{BB42A8EF-A444-40C2-BF4F-E156341E4127}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 1, (1, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IChemDrawDocument_vtables_dispatch_ = 1
IChemDrawDocument_vtables_ = [
	(( 'name' , 'retval' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FullName' , 'retval' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 4, (4, (), [ (16393, 10, None, "IID('{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Path' , 'retval' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ReadOnly' , 'retval' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Saved' , 'retval' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DataObject' , 'retval' , ), 8, (8, (), [ (16393, 10, None, "IID('{41A7D760-6018-11CF-9016-00AA0068841E}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Objects' , 'retval' , ), 9, (9, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Selection' , 'retval' , ), 10, (10, (), [ (16393, 10, None, "IID('{2590DD54-2A58-4A2A-AF35-5EE4CE3EABFA}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Settings' , 'pVal' , ), 11, (11, (), [ (16393, 10, None, "IID('{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Modified' , 'pVal' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Modified' , 'pVal' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( 'ShowCrosshair' , 'pVal' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowCrosshair' , 'pVal' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'ShowRulers' , 'pVal' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ShowRulers' , 'pVal' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'CaptionBeingEdited' , 'retval' , ), 17, (17, (), [ (16393, 10, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CaptionBeingEdited' , 'retval' , ), 17, (17, (), [ (9, 1, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DrawingSpace' , 'pVal' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DrawingSpace' , 'pVal' , ), 18, (18, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( 'Height' , 'pVal' , ), 19, (19, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'pVal' , ), 19, (19, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 64 , )),
	(( 'Width' , 'pVal' , ), 20, (20, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 20, (20, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 64 , )),
	(( 'NumPagesHigh' , 'pVal' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'NumPagesHigh' , 'pVal' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 64 , )),
	(( 'NumPagesWide' , 'pVal' , ), 22, (22, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'NumPagesWide' , 'pVal' , ), 22, (22, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 64 , )),
	(( 'Overlap' , 'pVal' , ), 23, (23, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Overlap' , 'pVal' , ), 23, (23, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 64 , )),
	(( 'PrintRegMarks' , 'pVal' , ), 24, (24, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'PrintRegMarks' , 'pVal' , ), 24, (24, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 64 , )),
	(( 'NumChemicalWarnings' , 'pVal' , ), 25, (25, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Magnification' , 'pVal' , ), 26, (26, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Magnification' , 'pVal' , ), 26, (26, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Annotations' , 'pVal' , ), 27, (27, (), [ (16393, 10, None, "IID('{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Atoms' , 'retval' , ), 301, (301, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Bonds' , 'retval' , ), 302, (302, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Graphics' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{D0E3D4B9-3B16-4331-BBA2-651319AE0402}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Splines' , 'retval' , ), 304, (304, (), [ (16393, 10, None, "IID('{272423F1-2909-4340-8870-8062530ADD05}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Captions' , 'retval' , ), 305, (305, (), [ (16393, 10, None, "IID('{D156092E-1412-458C-BD6A-3CC171B56E63}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Pictures' , 'retval' , ), 306, (306, (), [ (16393, 10, None, "IID('{41652842-15D6-44AE-AEFF-B51B179CF019}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Groups' , 'retval' , ), 307, (307, (), [ (16393, 10, None, "IID('{E5164832-7AFC-463A-9C19-A1AF6D191020}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Tables' , 'retval' , ), 308, (308, (), [ (16393, 10, None, "IID('{80C78566-D4BF-460E-B055-5728877FB30E}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'AltGroups' , 'retval' , ), 309, (309, (), [ (16393, 10, None, "IID('{D9E5D3D1-0D59-4126-B108-7D567E396FB3}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Geometries' , 'retval' , ), 310, (310, (), [ (16393, 10, None, "IID('{53C77081-53BF-4397-9BB4-84D6AF7C10F3}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'retval' , ), 311, (311, (), [ (16393, 10, None, "IID('{990C82BE-55F2-49F2-B822-2E448C7FEC80}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ReactionSchemes' , 'retval' , ), 312, (312, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'TLCPlates' , 'retval' , ), 313, (313, (), [ (16393, 10, None, "IID('{27609627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'StoichiometryGrids' , 'retval' , ), 314, (314, (), [ (16393, 10, None, "IID('{27109627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'PlasmidMaps' , 'retval' , ), 315, (315, (), [ (16393, 10, None, "IID('{E06B3507-3060-4095-8406-BAADD00A054E}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Arrows' , 'retval' , ), 316, (316, (), [ (16393, 10, None, "IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'retval' , ), 319, (319, (), [ (16393, 10, None, "IID('{D44C587D-2434-46B8-8B76-D309A2632456}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Brackets' , 'retval' , ), 320, (320, (), [ (16393, 10, None, "IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Activate' , ), 1610743820, (1610743820, (), [ ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Close' , 'saveChanges' , 'Filename' , ), 1610743821, (1610743821, (), [ (16396, 17, None, None) , 
			 (16396, 17, None, None) , ], 1 , 1 , 4 , 2 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Print' , 'from' , 'to' , 'copies' , ), 1610743822, (1610743822, (), [ 
			 (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 3 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Save' , ), 1610743823, (1610743823, (), [ ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'SaveAs' , 'Filename' , 'Format' , 'resolution' , 'Width' , 
			 'Height' , ), 1610743824, (1610743824, (), [ (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , 
			 (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 5 , 528 , (3, 0, None, None) , 0 , )),
	(( 'Undo' , ), 1610743825, (1610743825, (), [ ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'Redo' , ), 1610743826, (1610743826, (), [ ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Paste' , ), 1610743828, (1610743828, (), [ ], 1 , 1 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'PrintOut' , 'from' , 'to' , 'copies' , ), 1610743829, (1610743829, (), [ 
			 (16396, 17, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , ], 1 , 1 , 4 , 3 , 560 , (3, 0, None, None) , 0 , )),
	(( 'ZoomIn' , 'Center' , ), 1610743830, (1610743830, (), [ (9, 49, '0', "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ZoomOut' , 'Center' , ), 1610743831, (1610743831, (), [ (9, 49, '0', "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Zoom' , 'factor' , 'Center' , ), 1610743832, (1610743832, (), [ (5, 1, None, None) , 
			 (9, 49, '0', "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'MakeAtom' , 'pVal' , ), 401, (401, (), [ (16393, 10, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'MakeBond' , 'at1' , 'at2' , 'pVal' , ), 402, (402, (), [ 
			 (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , (16393, 10, None, "IID('{DADF0D97-73BC-4B3F-8FFD-047AF3635576}')") , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'MakeSpline' , 'pVal' , ), 404, (404, (), [ (16393, 10, None, "IID('{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')") , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'MakeCaption' , 'pVal' , ), 405, (405, (), [ (16393, 10, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'MakeGroup' , 'pVal' , ), 407, (407, (), [ (16393, 10, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'MakeTable' , 'pVal' , ), 408, (408, (), [ (16393, 10, None, "IID('{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')") , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'MakeAltGroup' , 'pVal' , ), 409, (409, (), [ (16393, 10, None, "IID('{D300E59D-D1B4-42D0-9112-730BDBA31EF2}')") , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'MakeGeometry' , 'geomType' , 'pVal' , ), 410, (410, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{A9173267-C525-4660-93A0-C5FF4BC55057}')") , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'MakeConstraint' , 'ConstraintType' , 'pVal' , ), 411, (411, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}')") , ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'MakeTLCPlate' , 'pVal' , ), 413, (413, (), [ (16393, 10, None, "IID('{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')") , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'MakeArrow' , 'pVal' , ), 414, (414, (), [ (16393, 10, None, "IID('{669C0868-90B0-4469-9621-7639880698B1}')") , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'MakeBracket' , 'type' , 'pVal' , ), 415, (415, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{CB61F475-A4BC-4307-9ED3-929BC4C694A0}')") , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'MakeSymbol' , 'type' , 'pVal' , ), 416, (416, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{0C9366BF-36BB-4303-86FA-966657FF891D}')") , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'MakeRectangle' , 'pVal' , ), 417, (417, (), [ (16393, 10, None, "IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')") , ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'MakeEllipse' , 'pVal' , ), 418, (418, (), [ (16393, 10, None, "IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')") , ], 1 , 1 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'MakeOrbital' , 'type' , 'pVal' , ), 419, (419, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')") , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'MakeStoichiometryGrid' , 'pVal' , ), 420, (420, (), [ (16393, 10, None, "IID('{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')") , ], 1 , 1 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'MakePlasmidMap' , 'pVal' , ), 421, (421, (), [ (16393, 10, None, "IID('{F06B3507-3060-4095-8406-CBBDD00A054E}')") , ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
]

IChemDrawDocuments_vtables_dispatch_ = 1
IChemDrawDocuments_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (16396, 17, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 1 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, "IID('{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'retval' , ), 1610743813, (1610743813, (), [ (16393, 10, None, "IID('{9E3A4685-0A8F-420D-A73E-4A37B83830DB}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Close' , ), 1610743814, (1610743814, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Open' , 'Filename' , 'password' , 'Format' , 'retval' , 
			 ), 1610743815, (1610743815, (), [ (8, 1, None, None) , (16396, 17, None, None) , (16396, 17, None, None) , (16393, 10, None, "IID('{9E3A4685-0A8F-420D-A73E-4A37B83830DB}')") , ], 1 , 1 , 4 , 2 , 112 , (3, 0, None, None) , 0 , )),
]

IChemDrawFragmentationAnalyzer_vtables_dispatch_ = 1
IChemDrawFragmentationAnalyzer_vtables_ = [
	(( 'MassFragments' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EECCC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationLines' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationAnalyzerType' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationAnalyzerType' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Owner' , 'pVal' , ), 5, (5, (), [ (16393, 10, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CurrentFragment' , 'pVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'HighlightNone' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SelectNone' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SelectAll' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'AutoUpdate' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AutoUpdate' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CurrentFragmentID' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IChemDrawFragmentationLine_vtables_dispatch_ = 1
IChemDrawFragmentationLine_vtables_ = [
	(( 'Spline' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CrossedBonds' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IChemDrawFragmentationLines_vtables_dispatch_ = 1
IChemDrawFragmentationLines_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawGeometries_vtables_dispatch_ = 1
IChemDrawGeometries_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{A9173267-C525-4660-93A0-C5FF4BC55057}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawGeometry_vtables_dispatch_ = 1
IChemDrawGeometry_vtables_ = [
	(( 'BasisObjects' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'GeometryType' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RelationValue' , 'pVal' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RelationValue' , 'pVal' , ), 103, (103, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IChemDrawGraphic_vtables_dispatch_ = 1
IChemDrawGraphic_vtables_ = [
	(( 'MajorAxisEnd' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'MajorAxisEnd' , 'pVal' , ), 101, (101, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'MinorAxisEnd' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'MinorAxisEnd' , 'pVal' , ), 102, (102, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GraphicType' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'LineType' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RectangleType' , 'pVal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'OvalType' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'OrbitalType' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'IsCircle' , 'pVal' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'IsOval' , 'pVal' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'IsOrbital' , 'pVal' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'IsRectangle' , 'pVal' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'IsRoundedRectangle' , 'pVal' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'IsBold' , 'pVal' , ), 113, (113, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'IsBold' , 'pVal' , ), 113, (113, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'IsDashed' , 'pVal' , ), 114, (114, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'IsDashed' , 'pVal' , ), 114, (114, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'IsFilled' , 'pVal' , ), 115, (115, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'IsFilled' , 'pVal' , ), 115, (115, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'IsShaded' , 'pVal' , ), 116, (116, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'IsShaded' , 'pVal' , ), 116, (116, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'IsShadowed' , 'pVal' , ), 117, (117, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'DelocalizedBonds' , 'pVal' , ), 118, (118, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IChemDrawGraphics_vtables_dispatch_ = 1
IChemDrawGraphics_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{24399466-10ED-4161-B216-1C57E5CE4F50}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawGroup_vtables_dispatch_ = 1
IChemDrawGroup_vtables_ = [
	(( 'Objects' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'GroupType' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Integral' , 'pVal' , ), 103, (103, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Integral' , 'pVal' , ), 103, (103, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'SequenceType' , 'pVal' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'SequenceType' , 'pVal' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Atoms' , 'retval' , ), 301, (301, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Bonds' , 'retval' , ), 302, (302, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Graphics' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{D0E3D4B9-3B16-4331-BBA2-651319AE0402}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Splines' , 'retval' , ), 304, (304, (), [ (16393, 10, None, "IID('{272423F1-2909-4340-8870-8062530ADD05}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Captions' , 'retval' , ), 305, (305, (), [ (16393, 10, None, "IID('{D156092E-1412-458C-BD6A-3CC171B56E63}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Pictures' , 'retval' , ), 306, (306, (), [ (16393, 10, None, "IID('{41652842-15D6-44AE-AEFF-B51B179CF019}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Groups' , 'retval' , ), 307, (307, (), [ (16393, 10, None, "IID('{E5164832-7AFC-463A-9C19-A1AF6D191020}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Tables' , 'retval' , ), 308, (308, (), [ (16393, 10, None, "IID('{80C78566-D4BF-460E-B055-5728877FB30E}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'AltGroups' , 'retval' , ), 309, (309, (), [ (16393, 10, None, "IID('{D9E5D3D1-0D59-4126-B108-7D567E396FB3}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Geometries' , 'retval' , ), 310, (310, (), [ (16393, 10, None, "IID('{53C77081-53BF-4397-9BB4-84D6AF7C10F3}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'retval' , ), 311, (311, (), [ (16393, 10, None, "IID('{990C82BE-55F2-49F2-B822-2E448C7FEC80}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ReactionSchemes' , 'retval' , ), 312, (312, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'TLCPlates' , 'retval' , ), 313, (313, (), [ (16393, 10, None, "IID('{27609627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'StoichiometryGrids' , 'retval' , ), 314, (314, (), [ (16393, 10, None, "IID('{27109627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'PlasmidMaps' , 'retval' , ), 315, (315, (), [ (16393, 10, None, "IID('{E06B3507-3060-4095-8406-BAADD00A054E}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Arrows' , 'retval' , ), 316, (316, (), [ (16393, 10, None, "IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'retval' , ), 319, (319, (), [ (16393, 10, None, "IID('{D44C587D-2434-46B8-8B76-D309A2632456}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Brackets' , 'retval' , ), 320, (320, (), [ (16393, 10, None, "IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationAnalyzer' , 'pVal' , 'retval' , ), 322, (322, (), [ (9, 1, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , 
			 (16393, 10, None, "IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2AAA}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
]

IChemDrawGroups_vtables_dispatch_ = 1
IChemDrawGroups_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawMassFragment_vtables_dispatch_ = 1
IChemDrawMassFragment_vtables_ = [
	(( 'ID' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Objects' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationLines' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BrokenBonds' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Highlighted' , 'pVal' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Highlighted' , 'pVal' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'pVal' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IChemDrawMassFragments_vtables_dispatch_ = 1
IChemDrawMassFragments_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawObject_vtables_dispatch_ = 1
IChemDrawObject_vtables_ = [
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Highlighted' , 'retval' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Highlighted' , 'retval' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'retval' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 5, (5, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 5, (5, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Selected' , 'pVal' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'index' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'index' , 'pVal' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Settings' , 'pVal' , ), 9, (9, (), [ (16393, 10, None, "IID('{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'WarningsIgnored' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'WarningsIgnored' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Bounds' , 'pVal' , ), 11, (11, (), [ (16393, 10, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 12, (12, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 12, (12, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'pVal' , ), 13, (13, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 14, (14, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'pVal' , ), 15, (15, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Bottom' , 'pVal' , ), 16, (16, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'pVal' , ), 17, (17, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Right' , 'pVal' , ), 18, (18, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , ), 19, (19, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'pVal' , ), 20, (20, (), [ (16393, 10, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Group' , 'pVal' , ), 20, (20, (), [ (9, 1, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Fragment' , 'pVal' , ), 21, (21, (), [ (16393, 10, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Fragment' , 'pVal' , ), 21, (21, (), [ (9, 1, None, "IID('{40957F2E-AC2D-44B4-B237-A7E2A825E636}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ObjectTags' , 'pVal' , ), 22, (22, (), [ (16393, 10, None, "IID('{05BE5E8B-5983-46E5-81A8-F80F5C21957A}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetObjectTag' , 'name' , 'pVal' , ), 23, (23, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{6DA748D4-4F21-45EA-BF09-F493643180F0}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'MakeObjectTag' , 'name' , 'duplicatesAllowed' , 'newTag' , ), 24, (24, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{6DA748D4-4F21-45EA-BF09-F493643180F0}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ChemicalWarning' , 'pVal' , ), 25, (25, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Annotations' , 'pVal' , ), 26, (26, (), [ (16393, 10, None, "IID('{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IChemDrawObjectTag_vtables_dispatch_ = 1
IChemDrawObjectTag_vtables_ = [
	(( 'caption' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ObjectTagType' , 'pVal' , ), 102, (102, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'DoubleValue' , 'retval' , ), 103, (103, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'DoubleValue' , 'retval' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'LongValue' , 'retval' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'LongValue' , 'retval' , ), 104, (104, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'StringValue' , 'retval' , ), 105, (105, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'StringValue' , 'retval' , ), 105, (105, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Owner' , 'retval' , ), 106, (106, (), [ (9, 1, None, "IID('{A341E650-F6F0-4068-B499-C231DDEBFBFD}')") , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Owner' , 'retval' , ), 106, (106, (), [ (16393, 10, None, "IID('{A341E650-F6F0-4068-B499-C231DDEBFBFD}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'PositioningType' , 'pVal' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'PositioningType' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'PositioningAngle' , 'pVal' , ), 108, (108, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'PositioningAngle' , 'pVal' , ), 108, (108, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'PositioningOffset' , 'pVal' , ), 109, (109, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'PositioningOffset' , 'pVal' , ), 109, (109, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Tracking' , 'retval' , ), 110, (110, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Tracking' , 'retval' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Persistent' , 'retval' , ), 111, (111, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Persistent' , 'retval' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
]

IChemDrawObjectTags_vtables_dispatch_ = 1
IChemDrawObjectTags_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{6DA748D4-4F21-45EA-BF09-F493643180F0}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawObjects_vtables_dispatch_ = 1
IChemDrawObjects_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ElementalAnalysis' , 'pVal' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ExactMass' , 'pVal' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Formula' , 'pVal' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MolecularWeight' , 'pVal' , ), 6, (6, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 7, (7, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{A341E650-F6F0-4068-B499-C231DDEBFBFD}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Select' , ), 9, (9, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Unselect' , ), 10, (10, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MapReactionAtoms' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ClearReactionMap' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Scale' , 'factor' , 'scaleLabels' , 'scaleSettings' , ), 13, (13, (), [ 
			 (5, 1, None, None) , (11, 49, 'True', None) , (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'pVal' , ), 14, (14, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 15, (15, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'pVal' , ), 16, (16, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Bottom' , 'pVal' , ), 17, (17, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'pVal' , ), 18, (18, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Right' , 'pVal' , ), 19, (19, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Clean' , 'deNovo' , ), 20, (20, (), [ (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Data' , 'dataType' , 'resolution' , 'Width' , 'Height' , 
			 'pVal' , ), 21, (21, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (16396, 10, None, None) , ], 1 , 2 , 4 , 4 , 232 , (3, 0, None, None) , 60 , )),
	(( 'Data' , 'dataType' , 'resolution' , 'Width' , 'Height' , 
			 'pVal' , ), 21, (21, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (16396, 10, None, None) , ], 1 , 2 , 4 , 4 , 232 , (3, 0, None, None) , 60 , )),
	(( 'Data' , 'dataType' , 'resolution' , 'Width' , 'Height' , 
			 'pVal' , ), 21, (21, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 60 , )),
	(( 'Data' , 'dataType' , 'resolution' , 'Width' , 'Height' , 
			 'pVal' , ), 21, (21, (), [ (12, 17, None, None) , (12, 17, None, None) , (12, 17, None, None) , 
			 (12, 17, None, None) , (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 60 , )),
	(( 'Settings' , 'pVal' , ), 22, (22, (), [ (16393, 10, None, "IID('{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Move' , 'dx' , 'dy' , ), 23, (23, (), [ (5, 49, '0.0', None) , 
			 (5, 49, '0.0', None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Join' , 'pVal' , ), 24, (24, (), [ (9, 1, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Rotate' , 'degrees' , 'rotateLabels' , ), 25, (25, (), [ (5, 1, None, None) , 
			 (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Flip' , 'vertical' , 'preservingAbsoluteStereochemistry' , ), 26, (26, (), [ (11, 49, 'False', None) , 
			 (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DataObject' , 'retval' , ), 27, (27, (), [ (16393, 10, None, "IID('{41A7D760-6018-11CF-9016-00AA0068841E}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FilterByTag' , 'tagName' , 'includeThese' , 'pVal' , ), 28, (28, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16393, 2, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FilterByTagDouble' , 'tagName' , 'tagValue' , 'includeThese' , 'pVal' , 
			 ), 29, (29, (), [ (8, 1, None, None) , (5, 1, None, None) , (11, 1, None, None) , (16393, 2, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'FilterByTagLong' , 'tagName' , 'tagValue' , 'includeThese' , 'pVal' , 
			 ), 30, (30, (), [ (8, 1, None, None) , (3, 1, None, None) , (11, 1, None, None) , (16393, 2, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'FilterByTagString' , 'tagName' , 'tagValue' , 'includeThese' , 'pVal' , 
			 ), 31, (31, (), [ (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , (16393, 2, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ScaleXYZ' , 'factorX' , 'factorY' , 'factorZ' , 'scaleLabels' , 
			 'scaleSettings' , ), 32, (32, (), [ (5, 1, None, None) , (5, 1, None, None) , (5, 49, '1.0', None) , 
			 (11, 49, 'True', None) , (11, 49, 'True', None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Bitmap' , 'pVal' , ), 33, (33, (), [ (16393, 10, None, "IID('{7BF80981-BF32-101A-8BBB-00AA00300CAB}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Metafile' , 'pVal' , ), 34, (34, (), [ (16393, 10, None, "IID('{7BF80981-BF32-101A-8BBB-00AA00300CAB}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'EnhancedMetafile' , 'pVal' , ), 35, (35, (), [ (16393, 10, None, "IID('{7BF80981-BF32-101A-8BBB-00AA00300CAB}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Copy' , ), 36, (36, (), [ ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Cut' , ), 37, (37, (), [ ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ContractObjectsToLabel' , 'bstrLabel' , ), 38, (38, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ExpandLabelsToStructure' , ), 39, (39, (), [ ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'MakeAttachedData' , 'name' , 'newText' , ), 40, (40, (), [ (8, 1, None, None) , 
			 (16393, 1, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'FormulaHTML' , 'pVal' , ), 41, (41, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'pVal' , ), 42, (42, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'pVal' , ), 43, (43, (), [ (9, 1, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Contains' , 'pVal' , 'retval' , ), 44, (44, (), [ (9, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Clone' , 'retval' , ), 45, (45, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Atoms' , 'retval' , ), 301, (301, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Bonds' , 'retval' , ), 302, (302, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Graphics' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{D0E3D4B9-3B16-4331-BBA2-651319AE0402}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Splines' , 'retval' , ), 304, (304, (), [ (16393, 10, None, "IID('{272423F1-2909-4340-8870-8062530ADD05}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Captions' , 'retval' , ), 305, (305, (), [ (16393, 10, None, "IID('{D156092E-1412-458C-BD6A-3CC171B56E63}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Pictures' , 'retval' , ), 306, (306, (), [ (16393, 10, None, "IID('{41652842-15D6-44AE-AEFF-B51B179CF019}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Groups' , 'retval' , ), 307, (307, (), [ (16393, 10, None, "IID('{E5164832-7AFC-463A-9C19-A1AF6D191020}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'Tables' , 'retval' , ), 308, (308, (), [ (16393, 10, None, "IID('{80C78566-D4BF-460E-B055-5728877FB30E}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'AltGroups' , 'retval' , ), 309, (309, (), [ (16393, 10, None, "IID('{D9E5D3D1-0D59-4126-B108-7D567E396FB3}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Geometries' , 'retval' , ), 310, (310, (), [ (16393, 10, None, "IID('{53C77081-53BF-4397-9BB4-84D6AF7C10F3}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'retval' , ), 311, (311, (), [ (16393, 10, None, "IID('{990C82BE-55F2-49F2-B822-2E448C7FEC80}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'ReactionSchemes' , 'retval' , ), 312, (312, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'TLCPlates' , 'retval' , ), 313, (313, (), [ (16393, 10, None, "IID('{27609627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'StoichiometryGrids' , 'retval' , ), 314, (314, (), [ (16393, 10, None, "IID('{27109627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'PlasmidMaps' , 'retval' , ), 315, (315, (), [ (16393, 10, None, "IID('{E06B3507-3060-4095-8406-BAADD00A054E}')") , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'Arrows' , 'retval' , ), 316, (316, (), [ (16393, 10, None, "IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')") , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'retval' , ), 319, (319, (), [ (16393, 10, None, "IID('{D44C587D-2434-46B8-8B76-D309A2632456}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Brackets' , 'retval' , ), 320, (320, (), [ (16393, 10, None, "IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')") , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
]

IChemDrawPicture_vtables_dispatch_ = 1
IChemDrawPicture_vtables_ = [
	(( 'PictureType' , 'pVal' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IChemDrawPictures_vtables_dispatch_ = 1
IChemDrawPictures_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{108A38A7-A0A1-4534-B59B-FFAEBC96D489}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawPlasmidMap_vtables_dispatch_ = 1
IChemDrawPlasmidMap_vtables_ = [
	(( 'Markers' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{ABCB3507-3060-4095-8406-B8BDD00A054E}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Plasmids' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{DEFB3507-3060-4095-8406-EEFDD00A054E}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'NumberBasePairs' , 'pVal' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'NumberBasePairs' , 'pVal' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'pVal' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'pVal' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'pVal' , ), 203, (203, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'pVal' , ), 203, (203, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'AddMarker' , 'retval' , ), 301, (301, (), [ (16393, 3, None, "IID('{F06B3507-3060-4095-8406-B8BDD00A054E}')") , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'AddPlasmid' , 'retval' , ), 302, (302, (), [ (16393, 3, None, "IID('{DEFB3507-3060-4095-8406-BBCDD00A054E}')") , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
]

IChemDrawPlasmidMaps_vtables_dispatch_ = 1
IChemDrawPlasmidMaps_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F06B3507-3060-4095-8406-CBBDD00A054E}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawPlasmidMarker_vtables_dispatch_ = 1
IChemDrawPlasmidMarker_vtables_ = [
	(( 'MarkerValue' , 'pVal' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'MarkerValue' , 'pVal' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pVal' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IChemDrawPlasmidMarkers_vtables_dispatch_ = 1
IChemDrawPlasmidMarkers_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F06B3507-3060-4095-8406-B8BDD00A054E}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawPlasmidRegion_vtables_dispatch_ = 1
IChemDrawPlasmidRegion_vtables_ = [
	(( 'RegionStart' , 'pVal' , ), 201, (201, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RegionStart' , 'pVal' , ), 201, (201, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RegionEnd' , 'pVal' , ), 202, (202, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RegionEnd' , 'pVal' , ), 202, (202, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pVal' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'pVal' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

IChemDrawPlasmidRegions_vtables_dispatch_ = 1
IChemDrawPlasmidRegions_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{DEFB3507-3060-4095-8406-BBCDD00A054E}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawPoint_vtables_dispatch_ = 1
IChemDrawPoint_vtables_ = [
	(( 'X' , 'pVal' , ), 1, (1, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'pVal' , ), 1, (1, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'pVal' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'pVal' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Z' , 'pVal' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Z' , 'pVal' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IChemDrawPreferences_vtables_dispatch_ = 1
IChemDrawPreferences_vtables_ = [
	(( 'Tolerance' , 'pVal' , ), 1, (1, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Tolerance' , 'pVal' , ), 1, (1, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ShowSlideGuides' , 'pVal' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ShowSlideGuides' , 'pVal' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RequireCtrlEnterLabel' , 'pVal' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RequireCtrlEnterLabel' , 'pVal' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RequireCtrlEnterCaption' , 'pVal' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RequireCtrlEnterCaption' , 'pVal' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticLabels' , 'pVal' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'AutomaticLabels' , 'pVal' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PrintBackgroundColor' , 'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'PrintBackgroundColor' , 'pVal' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CheckStructure' , 'pVal' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CheckStructure' , 'pVal' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShowAttachmentRank' , 'pVal' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowAttachmentRank' , 'pVal' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ShowReactionMap' , 'pVal' , ), 9, (9, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ShowReactionMap' , 'pVal' , ), 9, (9, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AutoReactionMap' , 'pVal' , ), 10, (10, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AutoReactionMap' , 'pVal' , ), 10, (10, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ShowStereochemistry' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ShowStereochemistry' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ShowChemicalWarning' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ShowChemicalWarning' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FixedLengths' , 'pVal' , ), 13, (13, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'FixedLengths' , 'pVal' , ), 13, (13, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'FixedAngles' , 'pVal' , ), 14, (14, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FixedAngles' , 'pVal' , ), 14, (14, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'IncludeDefaultFooter' , 'pVal' , ), 15, (15, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'IncludeDefaultFooter' , 'pVal' , ), 15, (15, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'AutoLassoSelection' , 'pVal' , ), 16, (16, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'AutoLassoSelection' , 'pVal' , ), 16, (16, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Units' , 'pVal' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Units' , 'pVal' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'TIFFColor' , 'pVal' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'TIFFColor' , 'pVal' , ), 18, (18, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'TIFFCompression' , 'pVal' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TIFFCompression' , 'pVal' , ), 19, (19, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'TIFFResolution' , 'pVal' , ), 20, (20, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'TIFFResolution' , 'pVal' , ), 20, (20, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'EPSBondQuality' , 'pVal' , ), 60, (60, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'EPSBondQuality' , 'pVal' , ), 60, (60, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'EPSColor' , 'pVal' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'EPSColor' , 'pVal' , ), 21, (21, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'EPSResolution' , 'pVal' , ), 22, (22, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'EPSResolution' , 'pVal' , ), 22, (22, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'TransparentGIFs' , 'pVal' , ), 23, (23, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'TransparentGIFs' , 'pVal' , ), 23, (23, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'AntialiasedGIFs' , 'pVal' , ), 24, (24, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'AntialiasedGIFs' , 'pVal' , ), 24, (24, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'PostScriptPreviewUsesWMF' , 'pVal' , ), 25, (25, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'PostScriptPreviewUsesWMF' , 'pVal' , ), 25, (25, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'PostScriptPreviewUsesTIFF' , 'pVal' , ), 26, (26, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'PostScriptPreviewUsesTIFF' , 'pVal' , ), 26, (26, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ChemicalWarningsToShow' , 'pVal' , ), 27, (27, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'ChemicalWarningsToShow' , 'pVal' , ), 27, (27, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'UseOpenFormat' , 'pVal' , ), 28, (28, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'UseOpenFormat' , 'pVal' , ), 28, (28, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'OpenFormat' , 'pVal' , ), 29, (29, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'OpenFormat' , 'pVal' , ), 29, (29, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'UseDocumentsDirectory' , 'pVal' , ), 30, (30, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'UseDocumentsDirectory' , 'pVal' , ), 30, (30, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'DocumentsDirectory' , 'pVal' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'DocumentsDirectory' , 'pVal' , ), 31, (31, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'ChemDrawItemsDirectory' , 'pVal' , ), 32, (32, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ChemDrawItemsDirectory' , 'pVal' , ), 32, (32, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'DefaultToolWhenOpeningDocuments' , 'pVal' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'DefaultToolWhenOpeningDocuments' , 'pVal' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'UseSaveFormat' , 'pVal' , ), 34, (34, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'UseSaveFormat' , 'pVal' , ), 34, (34, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'SaveFormat' , 'pVal' , ), 35, (35, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'SaveFormat' , 'pVal' , ), 35, (35, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'AutoSave' , 'pVal' , ), 36, (36, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'AutoSave' , 'pVal' , ), 36, (36, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'AutoSaveMinutes' , 'pVal' , ), 37, (37, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'AutoSaveMinutes' , 'pVal' , ), 37, (37, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'PromptForComment' , 'pVal' , ), 38, (38, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'PromptForComment' , 'pVal' , ), 38, (38, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'WarnAboutDataLoss' , 'pVal' , ), 39, (39, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'WarnAboutDataLoss' , 'pVal' , ), 39, (39, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'GraphicsOutputBorder' , 'pVal' , ), 40, (40, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'GraphicsOutputBorder' , 'pVal' , ), 40, (40, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'CheckFileExtensionsWhenLaunching' , 'pVal' , ), 41, (41, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'CheckFileExtensionsWhenLaunching' , 'pVal' , ), 41, (41, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'NMRHSolvent' , 'pVal' , ), 48, (48, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'NMRHSolvent' , 'pVal' , ), 48, (48, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'NMRHFrequency' , 'pVal' , ), 42, (42, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'NMRHFrequency' , 'pVal' , ), 42, (42, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'NMRHSystemData' , 'pVal' , ), 49, (49, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'NMRHSystemData' , 'pVal' , ), 49, (49, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'NMRHUserData' , 'pVal' , ), 50, (50, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'NMRHUserData' , 'pVal' , ), 50, (50, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'NMRCSystemData' , 'pVal' , ), 51, (51, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'NMRCSystemData' , 'pVal' , ), 51, (51, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'PNGResolution' , 'pVal' , ), 43, (43, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'PNGResolution' , 'pVal' , ), 43, (43, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationAnalyzerType' , 'pVal' , ), 44, (44, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationAnalyzerType' , 'pVal' , ), 44, (44, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationHighlightType' , 'pVal' , ), 45, (45, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationHighlightType' , 'pVal' , ), 45, (45, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationAutoUpdate' , 'pVal' , ), 46, (46, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'FragmentationAutoUpdate' , 'pVal' , ), 46, (46, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'TransparentPNGs' , 'pVal' , ), 52, (52, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'TransparentPNGs' , 'pVal' , ), 52, (52, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'RetainIUPACNumber' , 'pVal' , ), 53, (53, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'RetainIUPACNumber' , 'pVal' , ), 53, (53, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'ShowMDLTopLevelStereoFlags' , 'pVal' , ), 54, (54, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'ShowMDLTopLevelStereoFlags' , 'pVal' , ), 54, (54, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'UseESCForSKCFileFormat' , 'pVal' , ), 55, (55, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( 'UseESCForSKCFileFormat' , 'pVal' , ), 55, (55, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'HideAbsoluteStereoFlags' , 'pVal' , ), 56, (56, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( 'HideAbsoluteStereoFlags' , 'pVal' , ), 56, (56, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'SuppressSettingDefAbsESC' , 'pVal' , ), 57, (57, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'SuppressSettingDefAbsESC' , 'pVal' , ), 57, (57, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'ShowChiralInPlaceOfABS' , 'pVal' , ), 58, (58, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( 'ShowChiralInPlaceOfABS' , 'pVal' , ), 58, (58, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreTopLevelChiralFlag' , 'pVal' , ), 59, (59, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 984 , (3, 0, None, None) , 0 , )),
	(( 'IgnoreTopLevelChiralFlag' , 'pVal' , ), 59, (59, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'DisablePerspectiveStereoPerception' , 'pVal' , ), 47, (47, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'DisablePerspectiveStereoPerception' , 'pVal' , ), 47, (47, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
]

IChemDrawReactionScheme_vtables_dispatch_ = 1
IChemDrawReactionScheme_vtables_ = [
	(( 'ReactionSteps' , 'retval' , ), 1, (1, (), [ (16393, 10, None, "IID('{1AF22C1E-B493-4B09-93BF-CBF17E8E0C9E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ReactionSchemeType' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Reactants' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Products' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Intermediates' , 'pVal' , ), 5, (5, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Plusses' , 'pVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Arrows' , 'pVal' , ), 7, (7, (), [ (16393, 10, None, "IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IChemDrawReactionSchemes_vtables_dispatch_ = 1
IChemDrawReactionSchemes_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawReactionStep_vtables_dispatch_ = 1
IChemDrawReactionStep_vtables_ = [
	(( 'Reactants' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Products' , 'pVal' , ), 2, (2, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ObjectsAboveArrow' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ObjectsBelowArrow' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Plusses' , 'pVal' , ), 5, (5, (), [ (16393, 10, None, "IID('{17E5A261-238D-44B1-BE44-704C63DF60DC}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Arrow' , 'pVal' , ), 6, (6, (), [ (16393, 10, None, "IID('{669C0868-90B0-4469-9621-7639880698B1}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IChemDrawReactionStepComponents_vtables_dispatch_ = 1
IChemDrawReactionStepComponents_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawReactionSteps_vtables_dispatch_ = 1
IChemDrawReactionSteps_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{8CDB739E-0CC6-4801-9699-F75CED822069}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawRect_vtables_dispatch_ = 1
IChemDrawRect_vtables_ = [
	(( 'Top' , 'pVal' , ), 1, (1, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Top' , 'pVal' , ), 1, (1, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'pVal' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Left' , 'pVal' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Bottom' , 'pVal' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Bottom' , 'pVal' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Right' , 'pVal' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Right' , 'pVal' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'pVal' , ), 6, (6, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'pVal' , ), 6, (6, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TopLeft' , 'pVal' , ), 7, (7, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TopLeft' , 'pVal' , ), 7, (7, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TopRight' , 'pVal' , ), 8, (8, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TopRight' , 'pVal' , ), 8, (8, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BottomLeft' , 'pVal' , ), 9, (9, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BottomLeft' , 'pVal' , ), 9, (9, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'BottomRight' , 'pVal' , ), 10, (10, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BottomRight' , 'pVal' , ), 10, (10, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Center' , 'pVal' , ), 11, (11, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Center' , 'pVal' , ), 11, (11, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsEmpty' , 'pVal' , ), 13, (13, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Offset' , 'dx' , 'dy' , ), 101, (101, (), [ (5, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Inflate' , 'dx' , 'dy' , ), 102, (102, (), [ (5, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Deflate' , 'dx' , 'dy' , ), 103, (103, (), [ (5, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Intersection' , 'newVal' , ), 104, (104, (), [ (9, 1, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Overlaps' , 'newVal' , 'pVal' , ), 105, (105, (), [ (9, 1, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Union' , 'newVal' , ), 106, (106, (), [ (9, 1, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'IsWithin' , 'newVal' , 'pVal' , ), 107, (107, (), [ (9, 1, None, "IID('{F1D58CFF-BF62-4A96-9889-CF509CEE2134}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'PtInRect' , 'newVal' , 'pVal' , ), 108, (108, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

IChemDrawSGComponent_vtables_dispatch_ = 1
IChemDrawSGComponent_vtables_ = [
	(( 'Properties' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{2214F33B-47B7-4CD8-AC4D-1906F3719D70}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddProperty' , 'retval' , ), 201, (201, (), [ (16393, 3, None, "IID('{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IChemDrawSGComponents_vtables_dispatch_ = 1
IChemDrawSGComponents_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawSGProperties_vtables_dispatch_ = 1
IChemDrawSGProperties_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawSGProperty_vtables_dispatch_ = 1
IChemDrawSGProperty_vtables_ = [
	(( 'ID' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 10, (10, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 10, (10, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pVal' , ), 13, (13, (), [ (16393, 10, None, "IID('{6DA748D4-4F21-45EA-BF09-F493643180F0}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IChemDrawSelection_vtables_dispatch_ = 1
IChemDrawSelection_vtables_ = [
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DataObject' , 'retval' , ), 2, (2, (), [ (16393, 10, None, "IID('{41A7D760-6018-11CF-9016-00AA0068841E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Objects' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{488D02F8-B874-4EAF-9A12-07DD8C895CA0}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Atoms' , 'retval' , ), 301, (301, (), [ (16393, 10, None, "IID('{4A2B95A2-2332-433B-B081-39A2B87C781E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Bonds' , 'retval' , ), 302, (302, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Graphics' , 'retval' , ), 303, (303, (), [ (16393, 10, None, "IID('{D0E3D4B9-3B16-4331-BBA2-651319AE0402}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Splines' , 'retval' , ), 304, (304, (), [ (16393, 10, None, "IID('{272423F1-2909-4340-8870-8062530ADD05}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Captions' , 'retval' , ), 305, (305, (), [ (16393, 10, None, "IID('{D156092E-1412-458C-BD6A-3CC171B56E63}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Pictures' , 'retval' , ), 306, (306, (), [ (16393, 10, None, "IID('{41652842-15D6-44AE-AEFF-B51B179CF019}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Groups' , 'retval' , ), 307, (307, (), [ (16393, 10, None, "IID('{E5164832-7AFC-463A-9C19-A1AF6D191020}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Tables' , 'retval' , ), 308, (308, (), [ (16393, 10, None, "IID('{80C78566-D4BF-460E-B055-5728877FB30E}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'AltGroups' , 'retval' , ), 309, (309, (), [ (16393, 10, None, "IID('{D9E5D3D1-0D59-4126-B108-7D567E396FB3}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometries' , 'retval' , ), 310, (310, (), [ (16393, 10, None, "IID('{53C77081-53BF-4397-9BB4-84D6AF7C10F3}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Constraints' , 'retval' , ), 311, (311, (), [ (16393, 10, None, "IID('{990C82BE-55F2-49F2-B822-2E448C7FEC80}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ReactionSchemes' , 'retval' , ), 312, (312, (), [ (16393, 10, None, "IID('{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TLCPlates' , 'retval' , ), 313, (313, (), [ (16393, 10, None, "IID('{27609627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StoichiometryGrids' , 'retval' , ), 314, (314, (), [ (16393, 10, None, "IID('{27109627-9196-4F73-8D89-25FC8B9C9592}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PlasmidMaps' , 'retval' , ), 315, (315, (), [ (16393, 10, None, "IID('{E06B3507-3060-4095-8406-BAADD00A054E}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Arrows' , 'retval' , ), 316, (316, (), [ (16393, 10, None, "IID('{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Symbols' , 'retval' , ), 319, (319, (), [ (16393, 10, None, "IID('{D44C587D-2434-46B8-8B76-D309A2632456}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Brackets' , 'retval' , ), 320, (320, (), [ (16393, 10, None, "IID('{F54ABF8B-12C1-43E7-BADA-33442B3FB871}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IChemDrawSettings_vtables_dispatch_ = 1
IChemDrawSettings_vtables_ = [
	(( 'ChainAngle' , 'pVal' , ), 1, (1, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ChainAngle' , 'pVal' , ), 1, (1, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BondSpacing' , 'pVal' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BondSpacing' , 'pVal' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'HashSpacing' , 'pVal' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'HashSpacing' , 'pVal' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BondLength' , 'pVal' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BondLength' , 'pVal' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'LineWidth' , 'pVal' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'LineWidth' , 'pVal' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'BoldWidth' , 'pVal' , ), 6, (6, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'BoldWidth' , 'pVal' , ), 6, (6, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MarginWidth' , 'pVal' , ), 7, (7, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'MarginWidth' , 'pVal' , ), 7, (7, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LabelFont' , 'pVal' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LabelFont' , 'pVal' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LabelSize' , 'pVal' , ), 9, (9, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LabelSize' , 'pVal' , ), 9, (9, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LabelFace' , 'pVal' , ), 10, (10, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LabelFace' , 'pVal' , ), 10, (10, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'LabelJustification' , 'pVal' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LabelJustification' , 'pVal' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LabelLineHeight' , 'pVal' , ), 12, (12, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'LabelLineHeight' , 'pVal' , ), 12, (12, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CaptionFont' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CaptionFont' , 'pVal' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CaptionSize' , 'pVal' , ), 14, (14, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CaptionSize' , 'pVal' , ), 14, (14, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CaptionFace' , 'pVal' , ), 15, (15, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CaptionFace' , 'pVal' , ), 15, (15, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CaptionJustification' , 'pVal' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CaptionJustification' , 'pVal' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CaptionLineHeight' , 'pVal' , ), 17, (17, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CaptionLineHeight' , 'pVal' , ), 17, (17, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'InterpretChemically' , 'pVal' , ), 18, (18, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'InterpretChemically' , 'pVal' , ), 18, (18, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomQuery' , 'pVal' , ), 19, (19, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomQuery' , 'pVal' , ), 19, (19, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomStereo' , 'pVal' , ), 20, (20, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomStereo' , 'pVal' , ), 20, (20, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomNumber' , 'pVal' , ), 21, (21, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomNumber' , 'pVal' , ), 21, (21, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'ShowBondQuery' , 'pVal' , ), 22, (22, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'ShowBondQuery' , 'pVal' , ), 22, (22, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ShowBondStereo' , 'pVal' , ), 23, (23, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ShowBondStereo' , 'pVal' , ), 23, (23, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ShowBondRxn' , 'pVal' , ), 24, (24, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ShowBondRxn' , 'pVal' , ), 24, (24, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 25, (25, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 25, (25, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'BackgroundColor' , 'pVal' , ), 26, (26, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'BackgroundColor' , 'pVal' , ), 26, (26, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ApplySettings' , 'dataType' , 'newVal' , ), 27, (27, (), [ (12, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'ShowTerminalCarbonLabels' , 'pVal' , ), 28, (28, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ShowTerminalCarbonLabels' , 'pVal' , ), 28, (28, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'ShowNonTerminalCarbonLabels' , 'pVal' , ), 29, (29, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'ShowNonTerminalCarbonLabels' , 'pVal' , ), 29, (29, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'HideImplicitHydrogens' , 'pVal' , ), 30, (30, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'HideImplicitHydrogens' , 'pVal' , ), 30, (30, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomEnhancedStereo' , 'pVal' , ), 31, (31, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'ShowAtomEnhancedStereo' , 'pVal' , ), 31, (31, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'AminoAcidTermini' , 'pVal' , ), 32, (32, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'AminoAcidTermini' , 'pVal' , ), 32, (32, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'ShowSequenceTermini' , 'pVal' , ), 33, (33, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'ShowSequenceTermini' , 'pVal' , ), 33, (33, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ShowSequenceBonds' , 'pVal' , ), 34, (34, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'ShowSequenceBonds' , 'pVal' , ), 34, (34, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'ResidueWrapCount' , 'pVal' , ), 35, (35, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'ResidueWrapCount' , 'pVal' , ), 35, (35, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'ResidueBlockCount' , 'pVal' , ), 36, (36, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'ResidueBlockCount' , 'pVal' , ), 36, (36, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'ShowSequenceUnlinkedBranches' , 'pVal' , ), 39, (39, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'ShowSequenceUnlinkedBranches' , 'pVal' , ), 39, (39, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
]

IChemDrawSpline_vtables_dispatch_ = 1
IChemDrawSpline_vtables_ = [
	(( 'NumPoints' , 'pVal' , ), 101, (101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'NumPoints' , 'pVal' , ), 101, (101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'GetPoint' , 'index' , 'pVal' , ), 102, (102, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'SetPoint' , 'index' , 'newVal' , ), 103, (103, (), [ (3, 1, None, None) , 
			 (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'DelocalizedBonds' , 'pVal' , ), 104, (104, (), [ (16393, 10, None, "IID('{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadType' , 'pVal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadType' , 'pVal' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionAtStart' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionAtStart' , 'pVal' , ), 106, (106, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionAtEnd' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ArrowHeadPositionAtEnd' , 'pVal' , ), 107, (107, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'IsBold' , 'pVal' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'IsBold' , 'pVal' , ), 108, (108, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'IsDashed' , 'pVal' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'IsDashed' , 'pVal' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'HeadSize' , 'pVal' , ), 110, (110, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'HeadSize' , 'pVal' , ), 110, (110, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'HeadCenterSize' , 'pVal' , ), 111, (111, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'HeadCenterSize' , 'pVal' , ), 111, (111, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'HeadWidth' , 'pVal' , ), 112, (112, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'HeadWidth' , 'pVal' , ), 112, (112, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pVal' , ), 113, (113, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pVal' , ), 113, (113, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'LineType' , 'pVal' , ), 114, (114, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'LineType' , 'pVal' , ), 114, (114, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'FillType' , 'pVal' , ), 115, (115, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'FillType' , 'pVal' , ), 115, (115, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
]

IChemDrawSplines_vtables_dispatch_ = 1
IChemDrawSplines_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{380714EE-CEC4-43C7-9D98-1CA296E19AD3}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawStoichiometryGrid_vtables_dispatch_ = 1
IChemDrawStoichiometryGrid_vtables_ = [
	(( 'Components' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{BE1EA86E-C241-43B1-892B-05771CA47928}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IChemDrawStoichiometryGrids_vtables_dispatch_ = 1
IChemDrawStoichiometryGrids_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawSymbol_vtables_dispatch_ = 1
IChemDrawSymbol_vtables_ = [
	(( 'Start' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Start' , 'pVal' , ), 101, (101, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'End' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'End' , 'pVal' , ), 102, (102, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'SymbolType' , 'pVal' , ), 103, (103, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'IsRadical' , 'pVal' , ), 104, (104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'IsCharge' , 'pVal' , ), 105, (105, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'IsPositiveCharge' , 'pVal' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'IsNegativeCharge' , 'pVal' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
]

IChemDrawSymbols_vtables_dispatch_ = 1
IChemDrawSymbols_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{0C9366BF-36BB-4303-86FA-966657FF891D}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawTLCLane_vtables_dispatch_ = 1
IChemDrawTLCLane_vtables_ = [
	(( 'Spots' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{2224F33B-47B7-4CD8-AC4D-1906F3719D70}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddSpot' , 'retval' , ), 201, (201, (), [ (16393, 3, None, "IID('{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IChemDrawTLCLanes_vtables_dispatch_ = 1
IChemDrawTLCLanes_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawTLCPlate_vtables_dispatch_ = 1
IChemDrawTLCPlate_vtables_ = [
	(( 'Lanes' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{BEDEA86E-C241-43B1-892B-05771CA47928}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'TopLeft' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TopLeft' , 'pVal' , ), 102, (102, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'TopRight' , 'pVal' , ), 103, (103, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'TopRight' , 'pVal' , ), 103, (103, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'BottomLeft' , 'pVal' , ), 104, (104, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'BottomLeft' , 'pVal' , ), 104, (104, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'BottomRight' , 'pVal' , ), 105, (105, (), [ (16393, 10, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'BottomRight' , 'pVal' , ), 105, (105, (), [ (9, 1, None, "IID('{16E2B1FC-50AE-4226-A471-F4029D444BA3}')") , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'OriginFraction' , 'retval' , ), 106, (106, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'OriginFraction' , 'retval' , ), 106, (106, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'SolventFrontFraction' , 'retval' , ), 107, (107, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SolventFrontFraction' , 'retval' , ), 107, (107, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ShowOrigin' , 'retval' , ), 108, (108, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'ShowOrigin' , 'retval' , ), 108, (108, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ShowSolventFront' , 'retval' , ), 109, (109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'ShowSolventFront' , 'retval' , ), 109, (109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ShowBorders' , 'retval' , ), 110, (110, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'ShowBorders' , 'retval' , ), 110, (110, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ShowSideTicks' , 'retval' , ), 111, (111, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'ShowSideTicks' , 'retval' , ), 111, (111, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'Transparent' , 'retval' , ), 112, (112, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'Transparent' , 'retval' , ), 112, (112, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'AddLane' , 'retval' , ), 201, (201, (), [ (16393, 3, None, "IID('{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}')") , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IChemDrawTLCPlates_vtables_dispatch_ = 1
IChemDrawTLCPlates_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawTLCSpot_vtables_dispatch_ = 1
IChemDrawTLCSpot_vtables_ = [
	(( 'ID' , 'retval' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Rf' , 'retval' , ), 2, (2, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Rf' , 'retval' , ), 2, (2, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'retval' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'retval' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'retval' , ), 4, (4, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'retval' , ), 4, (4, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Tail' , 'retval' , ), 5, (5, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Tail' , 'retval' , ), 5, (5, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Bold' , 'pVal' , ), 6, (6, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Bold' , 'pVal' , ), 6, (6, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Dashed' , 'pVal' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Dashed' , 'pVal' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Filled' , 'pVal' , ), 8, (8, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Filled' , 'pVal' , ), 8, (8, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pVal' , ), 9, (9, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Spacing' , 'pVal' , ), 9, (9, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 10, (10, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 10, (10, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 11, (11, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 11, (11, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ShowRf' , 'pVal' , ), 12, (12, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ShowRf' , 'pVal' , ), 12, (12, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RfTag' , 'pVal' , ), 13, (13, (), [ (16393, 10, None, "IID('{6DA748D4-4F21-45EA-BF09-F493643180F0}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IChemDrawTLCSpots_vtables_dispatch_ = 1
IChemDrawTLCSpots_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawTable_vtables_dispatch_ = 1
IChemDrawTable_vtables_ = [
	(( 'Cells' , 'pVal' , ), 101, (101, (), [ (16393, 10, None, "IID('{26B98B2C-EE16-49FD-95E5-A8551149C0EF}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'AddRow' , 'newRowNum' , ), 102, (102, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'AddColumn' , 'newColumnNum' , ), 103, (103, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'DeleteRow' , 'rowNum' , ), 104, (104, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'DeleteColumn' , 'columnNum' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'NumRows' , 'pVal' , ), 106, (106, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'NumColumns' , 'pVal' , ), 107, (107, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IChemDrawTables_vtables_dispatch_ = 1
IChemDrawTables_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{C6812BB8-208C-4B0E-8393-FFE017B66A8E}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawText_vtables_dispatch_ = 1
IChemDrawText_vtables_ = [
	(( 'Text' , 'pVal' , ), 101, (101, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pVal' , ), 101, (101, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Styles' , 'pVal' , ), 102, (102, (), [ (9, 1, None, "IID('{B27DB485-6C90-45D2-82C1-7D2F55D73654}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Styles' , 'pVal' , ), 102, (102, (), [ (16393, 10, None, "IID('{B27DB485-6C90-45D2-82C1-7D2F55D73654}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'pVal' , ), 103, (103, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'pVal' , ), 103, (103, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'WrapWidth' , 'pVal' , ), 104, (104, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'WrapWidth' , 'pVal' , ), 104, (104, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Justification' , 'pVal' , ), 105, (105, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Justification' , 'pVal' , ), 105, (105, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'IsEmpty' , 'pVal' , ), 106, (106, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'IsCharge' , 'pVal' , ), 107, (107, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Atom' , 'pVal' , ), 108, (108, (), [ (9, 1, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Atom' , 'pVal' , ), 108, (108, (), [ (16393, 10, None, "IID('{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'Family' , 'retval' , ), 109, (109, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'Family' , 'retval' , ), 109, (109, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'pVal' , ), 110, (110, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'pVal' , ), 110, (110, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'Face' , 'pVal' , ), 111, (111, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Face' , 'pVal' , ), 111, (111, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'LineHeight' , 'pVal' , ), 112, (112, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'LineHeight' , 'pVal' , ), 112, (112, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
]

IChemDrawTextStyle_vtables_dispatch_ = 1
IChemDrawTextStyle_vtables_ = [
	(( 'StartChar' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'StartChar' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Family' , 'retval' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Family' , 'retval' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'pVal' , ), 3, (3, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'pVal' , ), 3, (3, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Face' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Face' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 5, (5, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 5, (5, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IChemDrawTextStyles_vtables_dispatch_ = 1
IChemDrawTextStyles_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{12A5FA9C-5C27-4006-9F31-0B91278D7F70}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemDrawTexts_vtables_dispatch_ = 1
IChemDrawTexts_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'pVal' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemOfficeMenu_vtables_dispatch_ = 1
IChemOfficeMenu_vtables_ = [
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'caption' , 'retval' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'caption' , 'retval' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Enabled' , 'retval' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Enabled' , 'retval' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'index' , 'retval' , ), 4, (4, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MenuItems' , 'retval' , ), 5, (5, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 6, (6, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IChemOfficeMenuBar_vtables_dispatch_ = 1
IChemOfficeMenuBar_vtables_ = [
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'index' , 'retval' , ), 2, (2, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Menus' , 'retval' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 4, (4, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IChemOfficeMenuBars_vtables_dispatch_ = 1
IChemOfficeMenuBars_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (2, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChemOfficeMenuItem_vtables_dispatch_ = 1
IChemOfficeMenuItem_vtables_ = [
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'caption' , 'retval' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'caption' , 'retval' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Checked' , 'retval' , ), 3, (3, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Checked' , 'retval' , ), 3, (3, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Enabled' , 'retval' , ), 4, (4, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Enabled' , 'retval' , ), 4, (4, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'index' , 'retval' , ), 5, (5, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 6, (6, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CommandID' , 'retval' , ), 7, (7, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IChemOfficeMenuItems_vtables_dispatch_ = 1
IChemOfficeMenuItems_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (16396, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'caption' , 'beforeIndex' , 'objectName' , 'itemType' , 
			 'retval' , ), 4, (4, (), [ (8, 1, None, None) , (16396, 1, None, None) , (16396, 17, None, None) , 
			 (16396, 17, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 2 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'index' , ), 5, (5, (), [ (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IChemOfficeMenus_vtables_dispatch_ = 1
IChemOfficeMenus_vtables_ = [
	(( '_NewEnum' , 'retval' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 1 , )),
	(( 'Application' , 'retval' , ), 1, (1, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'retval' , ), 2, (2, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Parent' , 'retval' , ), 3, (3, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Item' , 'index' , 'retval' , ), 0, (0, (), [ (16396, 1, None, None) , 
			 (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'caption' , 'beforeIndex' , 'retval' , ), 4, (4, (), [ 
			 (8, 1, None, None) , (16396, 1, None, None) , (16393, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Remove' , 'index' , ), 5, (5, (), [ (16396, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{86BE5C00-1B92-11D0-87CF-1020AFD1F1AF}' : IChemOfficeMenuBars,
	'{86BE5C02-1B92-11D0-87CF-1020AFD1F1AF}' : IChemOfficeMenuBar,
	'{86BE5C04-1B92-11D0-87CF-1020AFD1F1AF}' : IChemOfficeMenus,
	'{86BE5C06-1B92-11D0-87CF-1020AFD1F1AF}' : IChemOfficeMenu,
	'{86BE5C08-1B92-11D0-87CF-1020AFD1F1AF}' : IChemOfficeMenuItems,
	'{86BE5C0A-1B92-11D0-87CF-1020AFD1F1AF}' : IChemOfficeMenuItem,
	'{16E2B1FC-50AE-4226-A471-F4029D444BA3}' : IChemDrawPoint,
	'{F1D58CFF-BF62-4A96-9889-CF509CEE2134}' : IChemDrawRect,
	'{BB42A8EF-A444-40C2-BF4F-E156341E4127}' : IChemDrawDataType,
	'{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}' : IChemDrawDataTypes,
	'{4BC8155A-553E-4992-A555-FEEECB11CAB8}' : IChemDrawPreferences,
	'{41A7D761-6018-11CF-9016-00AA0068841E}' : DataObjectFiles,
	'{41A7D760-6018-11CF-9016-00AA0068841E}' : DataObject,
	'{488D02F8-B874-4EAF-9A12-07DD8C895CA0}' : IChemDrawObjects,
	'{A341E650-F6F0-4068-B499-C231DDEBFBFD}' : IChemDrawObject,
	'{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}' : IChemDrawSettings,
	'{40957F2E-AC2D-44B4-B237-A7E2A825E636}' : IChemDrawGroup,
	'{4A2B95A2-2332-433B-B081-39A2B87C781E}' : IChemDrawAtoms,
	'{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}' : IChemDrawAtom,
	'{D300E59D-D1B4-42D0-9112-730BDBA31EF2}' : IChemDrawAltGroup,
	'{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}' : IChemDrawText,
	'{B27DB485-6C90-45D2-82C1-7D2F55D73654}' : IChemDrawTextStyles,
	'{12A5FA9C-5C27-4006-9F31-0B91278D7F70}' : IChemDrawTextStyle,
	'{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}' : IChemDrawBonds,
	'{DADF0D97-73BC-4B3F-8FFD-047AF3635576}' : IChemDrawBond,
	'{D0E3D4B9-3B16-4331-BBA2-651319AE0402}' : IChemDrawGraphics,
	'{24399466-10ED-4161-B216-1C57E5CE4F50}' : IChemDrawGraphic,
	'{272423F1-2909-4340-8870-8062530ADD05}' : IChemDrawSplines,
	'{380714EE-CEC4-43C7-9D98-1CA296E19AD3}' : IChemDrawSpline,
	'{D156092E-1412-458C-BD6A-3CC171B56E63}' : IChemDrawTexts,
	'{41652842-15D6-44AE-AEFF-B51B179CF019}' : IChemDrawPictures,
	'{108A38A7-A0A1-4534-B59B-FFAEBC96D489}' : IChemDrawPicture,
	'{E5164832-7AFC-463A-9C19-A1AF6D191020}' : IChemDrawGroups,
	'{80C78566-D4BF-460E-B055-5728877FB30E}' : IChemDrawTables,
	'{C6812BB8-208C-4B0E-8393-FFE017B66A8E}' : IChemDrawTable,
	'{26B98B2C-EE16-49FD-95E5-A8551149C0EF}' : IChemDrawCells,
	'{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}' : IChemDrawCell,
	'{40553F42-5954-43F2-B154-188727D588E1}' : IChemDrawBorder,
	'{D9E5D3D1-0D59-4126-B108-7D567E396FB3}' : IChemDrawAltGroups,
	'{53C77081-53BF-4397-9BB4-84D6AF7C10F3}' : IChemDrawGeometries,
	'{A9173267-C525-4660-93A0-C5FF4BC55057}' : IChemDrawGeometry,
	'{990C82BE-55F2-49F2-B822-2E448C7FEC80}' : IChemDrawConstraints,
	'{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}' : IChemDrawConstraint,
	'{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}' : IChemDrawReactionSchemes,
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}' : IChemDrawReactionScheme,
	'{1AF22C1E-B493-4B09-93BF-CBF17E8E0C9E}' : IChemDrawReactionSteps,
	'{8CDB739E-0CC6-4801-9699-F75CED822069}' : IChemDrawReactionStep,
	'{17E5A261-238D-44B1-BE44-704C63DF60DC}' : IChemDrawReactionStepComponents,
	'{669C0868-90B0-4469-9621-7639880698B1}' : IChemDrawArrow,
	'{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}' : IChemDrawArrows,
	'{27609627-9196-4F73-8D89-25FC8B9C9592}' : IChemDrawTLCPlates,
	'{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}' : IChemDrawTLCPlate,
	'{BEDEA86E-C241-43B1-892B-05771CA47928}' : IChemDrawTLCLanes,
	'{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}' : IChemDrawTLCLane,
	'{2224F33B-47B7-4CD8-AC4D-1906F3719D70}' : IChemDrawTLCSpots,
	'{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}' : IChemDrawTLCSpot,
	'{6DA748D4-4F21-45EA-BF09-F493643180F0}' : IChemDrawObjectTag,
	'{27109627-9196-4F73-8D89-25FC8B9C9592}' : IChemDrawStoichiometryGrids,
	'{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}' : IChemDrawStoichiometryGrid,
	'{BE1EA86E-C241-43B1-892B-05771CA47928}' : IChemDrawSGComponents,
	'{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}' : IChemDrawSGComponent,
	'{2214F33B-47B7-4CD8-AC4D-1906F3719D70}' : IChemDrawSGProperties,
	'{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}' : IChemDrawSGProperty,
	'{E06B3507-3060-4095-8406-BAADD00A054E}' : IChemDrawPlasmidMaps,
	'{F06B3507-3060-4095-8406-CBBDD00A054E}' : IChemDrawPlasmidMap,
	'{ABCB3507-3060-4095-8406-B8BDD00A054E}' : IChemDrawPlasmidMarkers,
	'{F06B3507-3060-4095-8406-B8BDD00A054E}' : IChemDrawPlasmidMarker,
	'{DEFB3507-3060-4095-8406-EEFDD00A054E}' : IChemDrawPlasmidRegions,
	'{DEFB3507-3060-4095-8406-BBCDD00A054E}' : IChemDrawPlasmidRegion,
	'{D44C587D-2434-46B8-8B76-D309A2632456}' : IChemDrawSymbols,
	'{0C9366BF-36BB-4303-86FA-966657FF891D}' : IChemDrawSymbol,
	'{F54ABF8B-12C1-43E7-BADA-33442B3FB871}' : IChemDrawBrackets,
	'{CB61F475-A4BC-4307-9ED3-929BC4C694A0}' : IChemDrawBracket,
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2AAA}' : IChemDrawFragmentationAnalyzer,
	'{F745F388-8D27-4BE8-9A3E-A082E20EECCC}' : IChemDrawMassFragments,
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}' : IChemDrawMassFragment,
	'{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}' : IChemDrawFragmentationLines,
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}' : IChemDrawFragmentationLine,
	'{05BE5E8B-5983-46E5-81A8-F80F5C21957A}' : IChemDrawObjectTags,
	'{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}' : IChemDrawAnnotations,
	'{DBD6A772-8979-4049-A58A-AA8F5D56A779}' : IChemDrawAnnotation,
	'{2590DD54-2A58-4A2A-AF35-5EE4CE3EABFA}' : IChemDrawSelection,
	'{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}' : IChemDrawApplication,
	'{9E3A4685-0A8F-420D-A73E-4A37B83830DB}' : IChemDrawDocument,
	'{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}' : IChemDrawDocuments,
	'{A61082F6-DD43-4DF4-9B7C-C25B0024DB4D}' : Point,
	'{3A0F4F2C-92C7-4569-96B6-D608BCBAFD66}' : Rect,
	'{C172F840-938F-4A55-A732-4A036E3FBF3D}' : Application,
	'{41BA6D21-A02E-11CE-8FD9-0020AFD1F20C}' : DocumentWin,
	'{EFD13774-5475-4FE1-A9BC-32FACFC0FEF2}' : Documents,
	'{32488EE6-8194-4A7D-98DC-8F8B9E48293B}' : MenuBars,
	'{02C35511-5742-4351-AB70-C3B08FFFB38A}' : MenuBar,
	'{65109431-873E-4933-9C0C-3F98374EE919}' : Menus,
	'{52E62199-79D7-4279-8F36-CAAB57814C00}' : Menu,
	'{2F749F8C-CAC3-4E31-9877-A311AB601053}' : MenuItems,
	'{23F9462B-E682-4B4F-82A1-7BFF7B682B0E}' : MenuItem,
	'{7C97009F-5782-4C5B-8601-7784BDE3F73D}' : Preferences,
	'{200850C1-6797-4C1D-960D-7917936531EE}' : Object,
	'{75DC8A59-DF79-481D-82F6-0BA538978791}' : Objects,
	'{7AF6DD12-F154-4FAE-8437-3B51CD00A5DE}' : Selection,
	'{D8276FFA-D137-4E55-9A86-5E73A3407617}' : Atoms,
	'{2529F00D-9844-4F38-BDEB-6F59CFB816D7}' : Atom,
	'{ED49B2DA-B782-4C80-B10A-6929EF115652}' : Bonds,
	'{5A4404EB-85A0-46D1-9157-97796E11133E}' : Bond,
	'{05B8BA9A-2869-44AD-A3FB-A8D6F392F6FC}' : Graphics,
	'{637AB4EC-B34C-4708-B06A-E8E5922302AA}' : Graphic,
	'{54B822AD-CD66-452E-A985-F7A78AD09987}' : Arrows,
	'{0902D2BB-C8B3-4301-BE9C-D19443534718}' : Arrow,
	'{CC11162C-C954-4859-A9C4-37B6C06C3F4B}' : Brackets,
	'{5F717BE1-0415-4397-A493-F61E9315356D}' : Bracket,
	'{2470A7A4-3845-4AE3-8034-82F091367BF4}' : Symbols,
	'{2984EE75-82FC-46B2-AE1E-8A82C77F2DE1}' : Symbol,
	'{31D1265E-BF76-43FE-A7B0-257325B904B3}' : Splines,
	'{FEDAEFD6-F32A-40A8-97D5-8E5DF32425B3}' : Spline,
	'{70CE4755-9513-4C41-B4FB-CD7FADFABEC5}' : Styles,
	'{7F97C7DD-07E9-45D8-9B6D-EAC2C094336F}' : Style,
	'{08D68E3F-E1CB-4E6A-B7D8-8D27D4D0FF43}' : Captions,
	'{9B1B67CB-9794-4432-8F2D-766ED39AB5C4}' : caption,
	'{F5F5A846-177D-4987-8D57-B3A401618C04}' : ObjectTags,
	'{A6011FEC-EF26-417A-9E0F-DF9379873DAF}' : ObjectTag,
	'{24535E40-072D-4068-AA42-154513415BB3}' : Pictures,
	'{46CB2881-7626-4C35-A4D7-45F245CC8376}' : Picture,
	'{C7B5B8A1-F00F-4DDB-8DB9-C424E3342CF0}' : Border,
	'{504B85C3-4DA8-4C83-9C1D-C34C447491C7}' : Cells,
	'{4ABDA8EB-29B0-469D-B937-F213AA330CEC}' : Cell,
	'{DA47E69C-6A9A-4C52-8754-0158EC317F39}' : Tables,
	'{A803FB2E-9C62-4E72-8742-418C8892B15F}' : Table,
	'{188B972B-956D-4A92-BEDE-6B81D3232694}' : TLCSpots,
	'{D43B5DF8-89D0-4D7B-9811-F510AECB6798}' : TLCSpot,
	'{BE7FFDC2-A4B8-4B8E-99C9-9AB476904B5F}' : TLCLanes,
	'{22B44C17-01EC-471D-B15E-C40090786B54}' : TLCLane,
	'{F5EEC5B2-1756-455F-9F1F-59188D877D20}' : TLCPlates,
	'{1098F877-126F-44EB-8C26-D3A3E5286956}' : TLCPlate,
	'{181B972B-956D-4A92-BEDE-6B81D3232694}' : SGProperties,
	'{D41B5DF8-89D0-4D7B-9811-F510AECB6798}' : SGProperty,
	'{BE1FFDC2-A4B8-4B8E-99C9-9AB476904B5F}' : SGComponents,
	'{22144C17-01EC-471D-B15E-C40090786B54}' : SGComponent,
	'{F51EC5B2-1756-455F-9F1F-59188D877D20}' : StoichiometryGrids,
	'{1018F877-126F-44EB-8C26-D3A3E5286956}' : StoichiometryGrid,
	'{10840A43-1023-47A4-AD33-3C92B257DD61}' : PlasmidMarkers,
	'{DA5D0F99-162A-45B0-B81B-0F48A4781DE2}' : PlasmidMarker,
	'{2193B148-381B-486E-B96B-B21C6CD6AD02}' : PlasmidRegions,
	'{E0D25ABD-8210-4390-AF26-EC7B85C651FA}' : PlasmidRegion,
	'{E2CB8432-6642-4DEB-B956-A6A579922E80}' : PlasmidMaps,
	'{4B87F2A6-B4BD-4418-9610-0216BC7DC190}' : PlasmidMap,
	'{47CF6326-FBAF-49C9-BA9C-F6242EB52DC6}' : Groups,
	'{1C41DA07-5244-447F-AD57-43DCD32F88A5}' : Group,
	'{823B2C7E-8DC5-49BF-9FF1-F24F32A0B7AB}' : AltGroups,
	'{3CA7EAEC-2ED5-4E60-8261-D60CAA24F975}' : AltGroup,
	'{3DA3006C-EA2E-4E6C-A9C0-163A5774A3EF}' : Geometries,
	'{425C0C02-0AC8-48F4-A0F7-E6E7A61EDB2A}' : Geometry,
	'{A7E7C374-E261-414A-847C-ED92818617F9}' : Constraints,
	'{59D52749-0AE5-4AE5-A5BE-7534DA8DD900}' : Constraint,
	'{C1782781-382B-4D8F-84F7-D94AD34299FC}' : ReactionSchemes,
	'{8BC99E8A-2E32-449B-A22F-BFBE43903E91}' : ReactionScheme,
	'{9F8EDE4B-1872-4ABE-9255-1F3A49703F3E}' : ReactionSteps,
	'{125A7E5F-B055-45E0-894E-BFB0405809F7}' : ReactionStep,
	'{9A7B95B6-AA5B-4CC7-B996-D99989051F60}' : ReactionStepComponents,
	'{D716300D-8CBF-40FF-9C58-9CCEA0F34DDD}' : FragmentationAnalyzer,
	'{7D717A46-968E-47EB-B78E-C32DD437DFFF}' : MassFragments,
	'{D716300D-8CBF-40FF-9C58-9CCEA0F34FFF}' : MassFragment,
	'{7D717A46-968E-47EB-B78E-C32DD437EFFF}' : FragmentationLines,
	'{D716300D-8CBF-40FF-9C58-9CCEA0F3EFFF}' : FragmentationLine,
	'{290E5D0A-000C-405D-8E83-895CC9E3D8C4}' : Settings,
	'{1E1AC724-C06D-4078-9E42-DBB291BA236B}' : dataType,
	'{B8DAB55C-E0EC-4337-B1F0-D8ECABD6955F}' : DataTypes,
	'{AABDCC57-9D7B-4C81-9390-5703015A09E3}' : Annotations,
	'{DC1684DE-6A24-43AD-900C-BCE5150BB1F6}' : Annotation,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{86BE5C00-1B92-11D0-87CF-1020AFD1F1AF}' : 'IChemOfficeMenuBars',
	'{86BE5C02-1B92-11D0-87CF-1020AFD1F1AF}' : 'IChemOfficeMenuBar',
	'{86BE5C04-1B92-11D0-87CF-1020AFD1F1AF}' : 'IChemOfficeMenus',
	'{86BE5C06-1B92-11D0-87CF-1020AFD1F1AF}' : 'IChemOfficeMenu',
	'{86BE5C08-1B92-11D0-87CF-1020AFD1F1AF}' : 'IChemOfficeMenuItems',
	'{86BE5C0A-1B92-11D0-87CF-1020AFD1F1AF}' : 'IChemOfficeMenuItem',
	'{16E2B1FC-50AE-4226-A471-F4029D444BA3}' : 'IChemDrawPoint',
	'{F1D58CFF-BF62-4A96-9889-CF509CEE2134}' : 'IChemDrawRect',
	'{BB42A8EF-A444-40C2-BF4F-E156341E4127}' : 'IChemDrawDataType',
	'{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}' : 'IChemDrawDataTypes',
	'{4BC8155A-553E-4992-A555-FEEECB11CAB8}' : 'IChemDrawPreferences',
	'{41A7D761-6018-11CF-9016-00AA0068841E}' : 'DataObjectFiles',
	'{41A7D760-6018-11CF-9016-00AA0068841E}' : 'DataObject',
	'{488D02F8-B874-4EAF-9A12-07DD8C895CA0}' : 'IChemDrawObjects',
	'{A341E650-F6F0-4068-B499-C231DDEBFBFD}' : 'IChemDrawObject',
	'{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}' : 'IChemDrawSettings',
	'{40957F2E-AC2D-44B4-B237-A7E2A825E636}' : 'IChemDrawGroup',
	'{4A2B95A2-2332-433B-B081-39A2B87C781E}' : 'IChemDrawAtoms',
	'{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}' : 'IChemDrawAtom',
	'{D300E59D-D1B4-42D0-9112-730BDBA31EF2}' : 'IChemDrawAltGroup',
	'{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}' : 'IChemDrawText',
	'{B27DB485-6C90-45D2-82C1-7D2F55D73654}' : 'IChemDrawTextStyles',
	'{12A5FA9C-5C27-4006-9F31-0B91278D7F70}' : 'IChemDrawTextStyle',
	'{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}' : 'IChemDrawBonds',
	'{DADF0D97-73BC-4B3F-8FFD-047AF3635576}' : 'IChemDrawBond',
	'{D0E3D4B9-3B16-4331-BBA2-651319AE0402}' : 'IChemDrawGraphics',
	'{24399466-10ED-4161-B216-1C57E5CE4F50}' : 'IChemDrawGraphic',
	'{272423F1-2909-4340-8870-8062530ADD05}' : 'IChemDrawSplines',
	'{380714EE-CEC4-43C7-9D98-1CA296E19AD3}' : 'IChemDrawSpline',
	'{D156092E-1412-458C-BD6A-3CC171B56E63}' : 'IChemDrawTexts',
	'{41652842-15D6-44AE-AEFF-B51B179CF019}' : 'IChemDrawPictures',
	'{108A38A7-A0A1-4534-B59B-FFAEBC96D489}' : 'IChemDrawPicture',
	'{E5164832-7AFC-463A-9C19-A1AF6D191020}' : 'IChemDrawGroups',
	'{80C78566-D4BF-460E-B055-5728877FB30E}' : 'IChemDrawTables',
	'{C6812BB8-208C-4B0E-8393-FFE017B66A8E}' : 'IChemDrawTable',
	'{26B98B2C-EE16-49FD-95E5-A8551149C0EF}' : 'IChemDrawCells',
	'{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}' : 'IChemDrawCell',
	'{40553F42-5954-43F2-B154-188727D588E1}' : 'IChemDrawBorder',
	'{D9E5D3D1-0D59-4126-B108-7D567E396FB3}' : 'IChemDrawAltGroups',
	'{53C77081-53BF-4397-9BB4-84D6AF7C10F3}' : 'IChemDrawGeometries',
	'{A9173267-C525-4660-93A0-C5FF4BC55057}' : 'IChemDrawGeometry',
	'{990C82BE-55F2-49F2-B822-2E448C7FEC80}' : 'IChemDrawConstraints',
	'{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}' : 'IChemDrawConstraint',
	'{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}' : 'IChemDrawReactionSchemes',
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}' : 'IChemDrawReactionScheme',
	'{1AF22C1E-B493-4B09-93BF-CBF17E8E0C9E}' : 'IChemDrawReactionSteps',
	'{8CDB739E-0CC6-4801-9699-F75CED822069}' : 'IChemDrawReactionStep',
	'{17E5A261-238D-44B1-BE44-704C63DF60DC}' : 'IChemDrawReactionStepComponents',
	'{669C0868-90B0-4469-9621-7639880698B1}' : 'IChemDrawArrow',
	'{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}' : 'IChemDrawArrows',
	'{27609627-9196-4F73-8D89-25FC8B9C9592}' : 'IChemDrawTLCPlates',
	'{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}' : 'IChemDrawTLCPlate',
	'{BEDEA86E-C241-43B1-892B-05771CA47928}' : 'IChemDrawTLCLanes',
	'{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}' : 'IChemDrawTLCLane',
	'{2224F33B-47B7-4CD8-AC4D-1906F3719D70}' : 'IChemDrawTLCSpots',
	'{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}' : 'IChemDrawTLCSpot',
	'{6DA748D4-4F21-45EA-BF09-F493643180F0}' : 'IChemDrawObjectTag',
	'{27109627-9196-4F73-8D89-25FC8B9C9592}' : 'IChemDrawStoichiometryGrids',
	'{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}' : 'IChemDrawStoichiometryGrid',
	'{BE1EA86E-C241-43B1-892B-05771CA47928}' : 'IChemDrawSGComponents',
	'{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}' : 'IChemDrawSGComponent',
	'{2214F33B-47B7-4CD8-AC4D-1906F3719D70}' : 'IChemDrawSGProperties',
	'{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}' : 'IChemDrawSGProperty',
	'{E06B3507-3060-4095-8406-BAADD00A054E}' : 'IChemDrawPlasmidMaps',
	'{F06B3507-3060-4095-8406-CBBDD00A054E}' : 'IChemDrawPlasmidMap',
	'{ABCB3507-3060-4095-8406-B8BDD00A054E}' : 'IChemDrawPlasmidMarkers',
	'{F06B3507-3060-4095-8406-B8BDD00A054E}' : 'IChemDrawPlasmidMarker',
	'{DEFB3507-3060-4095-8406-EEFDD00A054E}' : 'IChemDrawPlasmidRegions',
	'{DEFB3507-3060-4095-8406-BBCDD00A054E}' : 'IChemDrawPlasmidRegion',
	'{D44C587D-2434-46B8-8B76-D309A2632456}' : 'IChemDrawSymbols',
	'{0C9366BF-36BB-4303-86FA-966657FF891D}' : 'IChemDrawSymbol',
	'{F54ABF8B-12C1-43E7-BADA-33442B3FB871}' : 'IChemDrawBrackets',
	'{CB61F475-A4BC-4307-9ED3-929BC4C694A0}' : 'IChemDrawBracket',
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2AAA}' : 'IChemDrawFragmentationAnalyzer',
	'{F745F388-8D27-4BE8-9A3E-A082E20EECCC}' : 'IChemDrawMassFragments',
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}' : 'IChemDrawMassFragment',
	'{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}' : 'IChemDrawFragmentationLines',
	'{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}' : 'IChemDrawFragmentationLine',
	'{05BE5E8B-5983-46E5-81A8-F80F5C21957A}' : 'IChemDrawObjectTags',
	'{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}' : 'IChemDrawAnnotations',
	'{DBD6A772-8979-4049-A58A-AA8F5D56A779}' : 'IChemDrawAnnotation',
	'{2590DD54-2A58-4A2A-AF35-5EE4CE3EABFA}' : 'IChemDrawSelection',
	'{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}' : 'IChemDrawApplication',
	'{9E3A4685-0A8F-420D-A73E-4A37B83830DB}' : 'IChemDrawDocument',
	'{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}' : 'IChemDrawDocuments',
}


NamesToIIDMap = {
	'IChemOfficeMenuBars' : '{86BE5C00-1B92-11D0-87CF-1020AFD1F1AF}',
	'IChemOfficeMenuBar' : '{86BE5C02-1B92-11D0-87CF-1020AFD1F1AF}',
	'IChemOfficeMenus' : '{86BE5C04-1B92-11D0-87CF-1020AFD1F1AF}',
	'IChemOfficeMenu' : '{86BE5C06-1B92-11D0-87CF-1020AFD1F1AF}',
	'IChemOfficeMenuItems' : '{86BE5C08-1B92-11D0-87CF-1020AFD1F1AF}',
	'IChemOfficeMenuItem' : '{86BE5C0A-1B92-11D0-87CF-1020AFD1F1AF}',
	'IChemDrawPoint' : '{16E2B1FC-50AE-4226-A471-F4029D444BA3}',
	'IChemDrawRect' : '{F1D58CFF-BF62-4A96-9889-CF509CEE2134}',
	'IChemDrawDataType' : '{BB42A8EF-A444-40C2-BF4F-E156341E4127}',
	'IChemDrawDataTypes' : '{CA581DB6-5E2D-402B-8FBD-432430CE7BBF}',
	'IChemDrawPreferences' : '{4BC8155A-553E-4992-A555-FEEECB11CAB8}',
	'DataObjectFiles' : '{41A7D761-6018-11CF-9016-00AA0068841E}',
	'DataObject' : '{41A7D760-6018-11CF-9016-00AA0068841E}',
	'IChemDrawObjects' : '{488D02F8-B874-4EAF-9A12-07DD8C895CA0}',
	'IChemDrawObject' : '{A341E650-F6F0-4068-B499-C231DDEBFBFD}',
	'IChemDrawSettings' : '{6AFCFA13-5595-49A9-8661-9013BF5FC1B7}',
	'IChemDrawGroup' : '{40957F2E-AC2D-44B4-B237-A7E2A825E636}',
	'IChemDrawAtoms' : '{4A2B95A2-2332-433B-B081-39A2B87C781E}',
	'IChemDrawAtom' : '{1EBA5945-0BC8-4303-85EA-1A3799FA74AC}',
	'IChemDrawAltGroup' : '{D300E59D-D1B4-42D0-9112-730BDBA31EF2}',
	'IChemDrawText' : '{FD6C48D5-3BF1-453B-A0F5-00F1D236F850}',
	'IChemDrawTextStyles' : '{B27DB485-6C90-45D2-82C1-7D2F55D73654}',
	'IChemDrawTextStyle' : '{12A5FA9C-5C27-4006-9F31-0B91278D7F70}',
	'IChemDrawBonds' : '{CF5E8FFD-2A61-4CEC-853C-BADD630FCAD6}',
	'IChemDrawBond' : '{DADF0D97-73BC-4B3F-8FFD-047AF3635576}',
	'IChemDrawGraphics' : '{D0E3D4B9-3B16-4331-BBA2-651319AE0402}',
	'IChemDrawGraphic' : '{24399466-10ED-4161-B216-1C57E5CE4F50}',
	'IChemDrawSplines' : '{272423F1-2909-4340-8870-8062530ADD05}',
	'IChemDrawSpline' : '{380714EE-CEC4-43C7-9D98-1CA296E19AD3}',
	'IChemDrawTexts' : '{D156092E-1412-458C-BD6A-3CC171B56E63}',
	'IChemDrawPictures' : '{41652842-15D6-44AE-AEFF-B51B179CF019}',
	'IChemDrawPicture' : '{108A38A7-A0A1-4534-B59B-FFAEBC96D489}',
	'IChemDrawGroups' : '{E5164832-7AFC-463A-9C19-A1AF6D191020}',
	'IChemDrawTables' : '{80C78566-D4BF-460E-B055-5728877FB30E}',
	'IChemDrawTable' : '{C6812BB8-208C-4B0E-8393-FFE017B66A8E}',
	'IChemDrawCells' : '{26B98B2C-EE16-49FD-95E5-A8551149C0EF}',
	'IChemDrawCell' : '{888119D9-EF6E-41FB-8F23-C6D9CA758EAD}',
	'IChemDrawBorder' : '{40553F42-5954-43F2-B154-188727D588E1}',
	'IChemDrawAltGroups' : '{D9E5D3D1-0D59-4126-B108-7D567E396FB3}',
	'IChemDrawGeometries' : '{53C77081-53BF-4397-9BB4-84D6AF7C10F3}',
	'IChemDrawGeometry' : '{A9173267-C525-4660-93A0-C5FF4BC55057}',
	'IChemDrawConstraints' : '{990C82BE-55F2-49F2-B822-2E448C7FEC80}',
	'IChemDrawConstraint' : '{9AA9B40D-DFD4-4B54-8FCA-64173157E2C3}',
	'IChemDrawReactionSchemes' : '{F745F388-8D27-4BE8-9A3E-A082E20EEBBC}',
	'IChemDrawReactionScheme' : '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2606}',
	'IChemDrawReactionSteps' : '{1AF22C1E-B493-4B09-93BF-CBF17E8E0C9E}',
	'IChemDrawReactionStep' : '{8CDB739E-0CC6-4801-9699-F75CED822069}',
	'IChemDrawReactionStepComponents' : '{17E5A261-238D-44B1-BE44-704C63DF60DC}',
	'IChemDrawArrow' : '{669C0868-90B0-4469-9621-7639880698B1}',
	'IChemDrawArrows' : '{9B7A4878-B6B0-4EA4-A85F-CD231785AE85}',
	'IChemDrawTLCPlates' : '{27609627-9196-4F73-8D89-25FC8B9C9592}',
	'IChemDrawTLCPlate' : '{AEBB4CE5-BCBE-4F51-850E-0564C67DE840}',
	'IChemDrawTLCLanes' : '{BEDEA86E-C241-43B1-892B-05771CA47928}',
	'IChemDrawTLCLane' : '{9EEAA3CF-C409-4B36-86B6-38FE7BACD504}',
	'IChemDrawTLCSpots' : '{2224F33B-47B7-4CD8-AC4D-1906F3719D70}',
	'IChemDrawTLCSpot' : '{9C2EEF24-D5D1-4455-BE47-4E58350F9ADA}',
	'IChemDrawObjectTag' : '{6DA748D4-4F21-45EA-BF09-F493643180F0}',
	'IChemDrawStoichiometryGrids' : '{27109627-9196-4F73-8D89-25FC8B9C9592}',
	'IChemDrawStoichiometryGrid' : '{AE1B4CE5-BCBE-4F51-850E-0564C67DE840}',
	'IChemDrawSGComponents' : '{BE1EA86E-C241-43B1-892B-05771CA47928}',
	'IChemDrawSGComponent' : '{9E1AA3CF-C409-4B36-86B6-38FE7BACD504}',
	'IChemDrawSGProperties' : '{2214F33B-47B7-4CD8-AC4D-1906F3719D70}',
	'IChemDrawSGProperty' : '{9C1EEF24-D5D1-4455-BE47-4E58350F9ADA}',
	'IChemDrawPlasmidMaps' : '{E06B3507-3060-4095-8406-BAADD00A054E}',
	'IChemDrawPlasmidMap' : '{F06B3507-3060-4095-8406-CBBDD00A054E}',
	'IChemDrawPlasmidMarkers' : '{ABCB3507-3060-4095-8406-B8BDD00A054E}',
	'IChemDrawPlasmidMarker' : '{F06B3507-3060-4095-8406-B8BDD00A054E}',
	'IChemDrawPlasmidRegions' : '{DEFB3507-3060-4095-8406-EEFDD00A054E}',
	'IChemDrawPlasmidRegion' : '{DEFB3507-3060-4095-8406-BBCDD00A054E}',
	'IChemDrawSymbols' : '{D44C587D-2434-46B8-8B76-D309A2632456}',
	'IChemDrawSymbol' : '{0C9366BF-36BB-4303-86FA-966657FF891D}',
	'IChemDrawBrackets' : '{F54ABF8B-12C1-43E7-BADA-33442B3FB871}',
	'IChemDrawBracket' : '{CB61F475-A4BC-4307-9ED3-929BC4C694A0}',
	'IChemDrawFragmentationAnalyzer' : '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2AAA}',
	'IChemDrawMassFragments' : '{F745F388-8D27-4BE8-9A3E-A082E20EECCC}',
	'IChemDrawMassFragment' : '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2CCC}',
	'IChemDrawFragmentationLines' : '{F745F388-8D27-4BE8-9A3E-A082E20EEDDD}',
	'IChemDrawFragmentationLine' : '{8E2B2FAB-AA3C-4ED1-8629-8436F42A2DDD}',
	'IChemDrawObjectTags' : '{05BE5E8B-5983-46E5-81A8-F80F5C21957A}',
	'IChemDrawAnnotations' : '{5910DE8D-28DB-4BF5-B0A0-4F2892428BCE}',
	'IChemDrawAnnotation' : '{DBD6A772-8979-4049-A58A-AA8F5D56A779}',
	'IChemDrawSelection' : '{2590DD54-2A58-4A2A-AF35-5EE4CE3EABFA}',
	'IChemDrawApplication' : '{2FA1A53F-5619-43BF-9FEE-3247E9AD987A}',
	'IChemDrawDocument' : '{9E3A4685-0A8F-420D-A73E-4A37B83830DB}',
	'IChemDrawDocuments' : '{46521D7D-0886-47DF-AFCF-7913C4CDCCF7}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

