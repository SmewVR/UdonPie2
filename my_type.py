from typing import *
from typing_extensions import Literal # 3.8: typing.Literal

# My Type Definition
VarName = NewType('VarName', str)
ValidStatus = Literal['NOT_EXIST', 'VALID', 'NOT_VALID']
# InitValue = Union[None, float, int, str]
FuncName = NewType('FuncName', str)
LabelName = NewType('LabelName', str)
Addr = NewType('Addr', int)
EventName = NewType('EventName', str)
UdonMethodName = NewType('UdonMethodName', str)
UdonMethodKind = Literal[
  'StaticFunc',
  'InstanceFunc',
  'Constructor', 
  'Unknown', 
]
ExternStr = NewType('ExternStr', str)

# UdonTypes
UdonTypeName = NewType('UdonTypeName', str)

UdonTypeName = Literal[
   'IEnumerableT',
   'SystemArray',
   'SystemBase64FormattingOptions',
   'SystemBoolean',
   'SystemBooleanArray',
   'SystemBooleanRef',
   'SystemByte',
   'SystemByteArray',
   'SystemByteRef',
   'SystemChar',
   'SystemCharArray',
   'SystemCharEnumerator',
   'SystemCharRef',
   'SystemCollectionsGenericIEnumerableSystemString',
   'SystemCollectionsGenericIEnumerableUnityEngineUIToggle',
   'SystemCollectionsGenericIEnumerableVRCSDKBaseVRC_EventHandlerVrcEvent',
   'SystemCollectionsGenericIListSystemCollectionsGenericKeyValuePairUnityEngineAnimationClipUnityEngineAnimationClip',
   'SystemCollectionsGenericListSystemCollectionsGenericKeyValuePairUnityEngineAnimationClipUnityEngineAnimationClip',
   'SystemCollectionsGenericListSystemInt32',
   'SystemCollectionsGenericListSystemSingle',
   'SystemCollectionsGenericListSystemString',
   'SystemCollectionsGenericListUnityEngineAnimationsConstraintSource',
   'SystemCollectionsGenericListUnityEngineAnimatorClipInfo',
   'SystemCollectionsGenericListUnityEngineBoneWeight',
   'SystemCollectionsGenericListUnityEngineColor',
   'SystemCollectionsGenericListUnityEngineColor32',
   'SystemCollectionsGenericListUnityEngineComponent',
   'SystemCollectionsGenericListUnityEngineEventSystemsRaycastResult',
   'SystemCollectionsGenericListUnityEngineMaterial',
   'SystemCollectionsGenericListUnityEngineMatrix4x4',
   'SystemCollectionsGenericListUnityEngineParticleSystemParticle',
   'SystemCollectionsGenericListUnityEngineRenderingSphericalHarmonicsL2',
   'SystemCollectionsGenericListUnityEngineSprite',
   'SystemCollectionsGenericListUnityEngineUIDropdownOptionData',
   'SystemCollectionsGenericListUnityEngineUIRectMask2D',
   'SystemCollectionsGenericListUnityEngineUISelectable',
   'SystemCollectionsGenericListUnityEngineUIVertex',
   'SystemCollectionsGenericListUnityEngineVector2',
   'SystemCollectionsGenericListUnityEngineVector3',
   'SystemCollectionsGenericListUnityEngineVector4',
   'SystemCollectionsGenericListVRCSDKBaseVRCPlayerApi',
   'SystemCollectionsIEnumerator',
   'SystemCollectionsObjectModelReadOnlyCollectionSystemTimeZoneInfo',
   'SystemConvert',
   'SystemDateTime',
   'SystemDateTimeArray',
   'SystemDateTimeKind',
   'SystemDateTimeOffset',
   'SystemDateTimeRef',
   'SystemDayOfWeek',
   'SystemDecimal',
   'SystemDouble',
   'SystemDoubleArray',
   'SystemDoubleRef',
   'SystemException',
   'SystemFuncUnityEngineUIILayoutElementSystemSingle',
   'SystemGlobalizationCompareOptions',
   'SystemGlobalizationCultureInfo',
   'SystemGlobalizationDateTimeStyles',
   'SystemGlobalizationNumberStyles',
   'SystemGlobalizationUnicodeCategory',
   'SystemGuid',
   'SystemIFormatProvider',
   'SystemInt16',
   'SystemInt16Array',
   'SystemInt16Ref',
   'SystemInt32',
   'SystemInt32Array',
   'SystemInt32ArrayRef',
   'SystemInt32Ref',
   'SystemInt64',
   'SystemInt64Array',
   'SystemInt64Ref',
   'SystemObject',
   'SystemObjectArray',
   'SystemObjectRef',
   'SystemRuntimeInteropServicesStructLayoutAttribute',
   'SystemRuntimeTypeHandle',
   'SystemSByte',
   'SystemSByteArray',
   'SystemSByteRef',
   'SystemSingle',
   'SystemSingleArray',
   'SystemSingleRef',
   'SystemSingle[]',
   'SystemString',
   'SystemStringArray',
   'SystemStringComparison',
   'SystemStringRef',
   'SystemStringSplitOptions',
   'SystemTextNormalizationForm',
   'SystemTimeSpan',
   'SystemTimeSpanArray',
   'SystemTimeZoneInfo',
   'SystemTimeZoneInfoAdjustmentRuleArray',
   'SystemTimeZoneInfoArray',
   'SystemTimeZoneInfoRef',
   'SystemType',
   'SystemTypeArray',
   'SystemTypeCode',
   'SystemTypeRef',
   'SystemUInt16',
   'SystemUInt16Array',
   'SystemUInt16Ref',
   'SystemUInt32',
   'SystemUInt32Array',
   'SystemUInt32Ref',
   'SystemUInt64',
   'SystemUInt64Array',
   'SystemUInt64Ref',
   'UnityEngineAINavMesh',
   'UnityEngineAINavMeshAgent',
   'UnityEngineAINavMeshAgentArray',
   'UnityEngineAINavMeshAgentRef',
   'UnityEngineAINavMeshBuildSettings',
   'UnityEngineAINavMeshData',
   'UnityEngineAINavMeshDataArray',
   'UnityEngineAINavMeshDataInstance',
   'UnityEngineAINavMeshDataRef',
   'UnityEngineAINavMeshHitRef',
   'UnityEngineAINavMeshLinkData',
   'UnityEngineAINavMeshLinkInstance',
   'UnityEngineAINavMeshObstacle',
   'UnityEngineAINavMeshObstacleArray',
   'UnityEngineAINavMeshObstacleRef',
   'UnityEngineAINavMeshObstacleShape',
   'UnityEngineAINavMeshPath',
   'UnityEngineAINavMeshPathArray',
   'UnityEngineAINavMeshPathRef',
   'UnityEngineAINavMeshPathStatus',
   'UnityEngineAINavMeshQueryFilter',
   'UnityEngineAINavMeshTriangulation',
   'UnityEngineAIObstacleAvoidanceType',
  'UnityEngineAIOffMeshLink',
   'UnityEngineAIOffMeshLinkArray',
   'UnityEngineAIOffMeshLinkData',
   'UnityEngineAIOffMeshLinkRef',
   'UnityEngineAccelerationEvent',
   'UnityEngineAccelerationEventArray',
   'UnityEngineAdditionalCanvasShaderChannels',
   'UnityEngineAnimation',
   'UnityEngineAnimationArray',
   'UnityEngineAnimationBlendMode',
   'UnityEngineAnimationClip',
   'UnityEngineAnimationClipArray',
   'UnityEngineAnimationClipRef',
   'UnityEngineAnimationCullingType',
   'UnityEngineAnimationCurve',
   'UnityEngineAnimationEvent',
   'UnityEngineAnimationEventArray',
   'UnityEngineAnimationPlayMode',
   'UnityEngineAnimationRef',
   'UnityEngineAnimationState',
   'UnityEngineAnimationStateArray',
   'UnityEngineAnimationStateRef',
   'UnityEngineAnimationsAimConstraint',
   'UnityEngineAnimationsAimConstraintArray',
   'UnityEngineAnimationsAimConstraintRef',
   'UnityEngineAnimationsAimConstraintWorldUpType',
   'UnityEngineAnimationsAxis',
   'UnityEngineAnimationsConstraintSource',
   'UnityEngineAnimationsConstraintSourceArray',
   'UnityEngineAnimationsConstraintSourceRef',
   'UnityEngineAnimationsLookAtConstraint',
   'UnityEngineAnimationsLookAtConstraintArray',
   'UnityEngineAnimationsLookAtConstraintRef',
   'UnityEngineAnimationsParentConstraint',
   'UnityEngineAnimationsParentConstraintArray',
   'UnityEngineAnimationsParentConstraintRef',
   'UnityEngineAnimationsPositionConstraint',
   'UnityEngineAnimationsPositionConstraintArray',
   'UnityEngineAnimationsPositionConstraintRef',
  'UnityEngineAnimationsRotationConstraint',
   'UnityEngineAnimationsRotationConstraintArray',
   'UnityEngineAnimationsRotationConstraintRef',
   'UnityEngineAnimationsScaleConstraint',
   'UnityEngineAnimationsScaleConstraintArray',
   'UnityEngineAnimationsScaleConstraintRef',
   'UnityEngineAnimator',
   'UnityEngineAnimatorArray',
   'UnityEngineAnimatorClipInfo',
   'UnityEngineAnimatorClipInfoArray',
   'UnityEngineAnimatorClipInfoRef',
   'UnityEngineAnimatorControllerParameter',
   'UnityEngineAnimatorControllerParameterArray',
   'UnityEngineAnimatorControllerParameterRef',
   'UnityEngineAnimatorControllerParameterType',
   'UnityEngineAnimatorCullingMode',
   'UnityEngineAnimatorOverrideController',
   'UnityEngineAnimatorOverrideControllerArray',
   'UnityEngineAnimatorOverrideControllerRef',
   'UnityEngineAnimatorRecorderMode',
   'UnityEngineAnimatorRef',
   'UnityEngineAnimatorStateInfo',
   'UnityEngineAnimatorStateInfoArray',
   'UnityEngineAnimatorStateInfoRef',
   'UnityEngineAnimatorTransitionInfo',
   'UnityEngineAnimatorTransitionInfoArray',
   'UnityEngineAnimatorTransitionInfoRef',
   'UnityEngineAnimatorUpdateMode',
   'UnityEngineAnimatorUtility',
   'UnityEngineAnimatorUtilityArray',
   'UnityEngineAnimatorUtilityRef',
   'UnityEngineAnisotropicFiltering',
   'UnityEngineAreaEffector2D',
   'UnityEngineAreaEffector2DArray',
   'UnityEngineAreaEffector2DRef',
   'UnityEngineAudioAudioMixerGroup',
   'UnityEngineAudioChorusFilter',
   'UnityEngineAudioChorusFilterArray',
   'UnityEngineAudioChorusFilterRef',
   'UnityEngineAudioClip',
   'UnityEngineAudioClipArray',
   'UnityEngineAudioClipLoadType',
   'UnityEngineAudioClipPCMReaderCallback',
   'UnityEngineAudioClipPCMSetPositionCallback',
   'UnityEngineAudioClipRef',
   'UnityEngineAudioDataLoadState',
   'UnityEngineAudioDistortionFilter',
   'UnityEngineAudioDistortionFilterArray',
   'UnityEngineAudioDistortionFilterRef',
   'UnityEngineAudioEchoFilter',
   'UnityEngineAudioEchoFilterArray',
   'UnityEngineAudioEchoFilterRef',
   'UnityEngineAudioHighPassFilter',
   'UnityEngineAudioHighPassFilterArray',
   'UnityEngineAudioHighPassFilterRef',
   'UnityEngineAudioLowPassFilter',
   'UnityEngineAudioLowPassFilterArray',
   'UnityEngineAudioLowPassFilterRef',
   'UnityEngineAudioReverbFilter',
   'UnityEngineAudioReverbFilterArray',
   'UnityEngineAudioReverbFilterRef',
   'UnityEngineAudioReverbPreset',
   'UnityEngineAudioReverbZone',
   'UnityEngineAudioReverbZoneArray',
   'UnityEngineAudioReverbZoneRef',
   'UnityEngineAudioRolloffMode',
   'UnityEngineAudioSource',
   'UnityEngineAudioSourceArray',
   'UnityEngineAudioSourceCurveType',
   'UnityEngineAudioSourceRef',
   'UnityEngineAudioVelocityUpdateMode',
   'UnityEngineAvatar',
   'UnityEngineAvatarArray',
   'UnityEngineAvatarBuilder',
   'UnityEngineAvatarBuilderArray',
   'UnityEngineAvatarBuilderRef',
   'UnityEngineAvatarIKGoal',
   'UnityEngineAvatarIKHint',
   'UnityEngineAvatarMask',
   'UnityEngineAvatarMaskArray',
   'UnityEngineAvatarMaskBodyPart',
   'UnityEngineAvatarMaskRef',
  'UnityEngineAvatarRef',
   'UnityEngineAvatarTarget',
   'UnityEngineBillboardAsset',
   'UnityEngineBillboardRenderer',
   'UnityEngineBillboardRendererArray',
   'UnityEngineBillboardRendererRef',
   'UnityEngineBlendWeights',
   'UnityEngineBoneWeightArray',
   'UnityEngineBounds',
   'UnityEngineBoundsArray',
   'UnityEngineBoundsRef',
   'UnityEngineBoxCollider',
   'UnityEngineBoxCollider2D',
   'UnityEngineBoxCollider2DArray',
   'UnityEngineBoxCollider2DRef',
   'UnityEngineBoxColliderArray',
   'UnityEngineBoxColliderRef',
   'UnityEngineCamera',
   'UnityEngineCameraArray',
   'UnityEngineCameraClearFlags',
   'UnityEngineCameraGateFitMode',
  'UnityEngineCameraGateFitParameters',
   'UnityEngineCameraMonoOrStereoscopicEye',
   'UnityEngineCameraRef',
   'UnityEngineCameraStereoscopicEye',
   'UnityEngineCameraType',
   'UnityEngineCanvas',
   'UnityEngineCanvasArray',
  'UnityEngineCanvasRef',
   'UnityEngineCanvasRenderer',
   'UnityEngineCanvasRendererArray',
   'UnityEngineCanvasRendererRef',
   'UnityEngineCanvasWillRenderCanvases',
   'UnityEngineCapsuleCollider',
  'UnityEngineCapsuleCollider2D',
   'UnityEngineCapsuleCollider2DArray',
   'UnityEngineCapsuleCollider2DRef',
   'UnityEngineCapsuleColliderArray',
   'UnityEngineCapsuleColliderRef',
   'UnityEngineCapsuleDirection2D',
   'UnityEngineCircleCollider2D',
   'UnityEngineCircleCollider2DArray',
   'UnityEngineCircleCollider2DRef',
   'UnityEngineCollider',
   'UnityEngineCollider2D',
   'UnityEngineCollider2DArray',
   'UnityEngineCollider2DRef',
   'UnityEngineColliderArray',
   'UnityEngineColliderDistance2D',
   'UnityEngineColliderRef',
   'UnityEngineCollision',
   'UnityEngineCollision2D',
   'UnityEngineCollision2DArray',   'UnityEngineCollision2DRef',
   'UnityEngineCollisionArray',
   'UnityEngineCollisionDetectionMode',
   'UnityEngineCollisionDetectionMode2D',
   'UnityEngineCollisionRef',
   'UnityEngineColor',
   'UnityEngineColor32',
  'UnityEngineColor32Array',
   'UnityEngineColorArray',
   'UnityEngineColorRef',
   'UnityEngineColorSpace',
   'UnityEngineCombineInstanceArray',
   'UnityEngineCompass',
   'UnityEngineComponent',
   'UnityEngineComponentArray',
   'UnityEngineComponentRef',
   'UnityEngineCompositeCollider2D',
   'UnityEngineCompositeCollider2DArray',
   'UnityEngineCompositeCollider2DGenerationType',
   'UnityEngineCompositeCollider2DGeometryType',
   'UnityEngineCompositeCollider2DRef',
   'UnityEngineComputeBuffer',
   'UnityEngineConfigurableJoint',
   'UnityEngineConfigurableJointArray',
   'UnityEngineConfigurableJointMotion',
   'UnityEngineConfigurableJointRef',
   'UnityEngineConstantForce',
   'UnityEngineConstantForce2D',
   'UnityEngineConstantForce2DArray',
   'UnityEngineConstantForce2DRef',
   'UnityEngineConstantForceArray',
   'UnityEngineConstantForceRef',
   'UnityEngineContactFilter2D',
   'UnityEngineContactPoint',
   'UnityEngineContactPoint2D',
   'UnityEngineContactPoint2DArray',
   'UnityEngineContactPoint2DRef',
   'UnityEngineContactPointArray',
   'UnityEngineContactPointRef',
   'UnityEngineCoroutine',
   'UnityEngineCubemap',
   'UnityEngineDebug',
   'UnityEngineDebugArray',
   'UnityEngineDebugRef',
   'UnityEngineDepthTextureMode',
   'UnityEngineDeviceOrientation',
   'UnityEngineDistanceJoint2D',
   'UnityEngineDistanceJoint2DArray',
   'UnityEngineDistanceJoint2DRef',
   'UnityEngineDurationUnit',
   'UnityEngineEdgeCollider2D',
   'UnityEngineEdgeCollider2DArray',
   'UnityEngineEdgeCollider2DRef',
   'UnityEngineEffector2D',
   'UnityEngineEffector2DArray',
   'UnityEngineEffector2DRef',
   'UnityEngineEffectorForceMode2D',
   'UnityEngineEffectorSelection2D',
   'UnityEngineEvent',
   'UnityEngineEventSystemsAxisEventData',
   'UnityEngineEventSystemsBaseEventData',
   'UnityEngineEventSystemsPointerEventData',
   'UnityEngineEventsUnityAction',
   'UnityEngineEventsUnityActionSystemBoolean',
   'UnityEngineEventsUnityActionSystemInt32',
   'UnityEngineEventsUnityActionSystemSingle',
   'UnityEngineEventsUnityActionSystemString',
   'UnityEngineEventsUnityActionUnityEngineVector2',
   'UnityEngineEventsUnityEventCallState',
   'UnityEngineExperimentalAnimationsMuscleHandle',
   'UnityEngineExperimentalAnimationsMuscleHandleArray',
   'UnityEngineExperimentalAnimationsMuscleHandleRef',
   'UnityEngineFFTWindow',
   'UnityEngineFixedJoint',
   'UnityEngineFixedJoint2D',
   'UnityEngineFixedJoint2DArray',
   'UnityEngineFixedJoint2DRef',
   'UnityEngineFixedJointArray',
   'UnityEngineFixedJointRef',
   'UnityEngineFlare',
   'UnityEngineFogMode',
   'UnityEngineFont',
   'UnityEngineFontStyle',
   'UnityEngineForceMode',
   'UnityEngineForceMode2D',
   'UnityEngineFrictionJoint2D',
   'UnityEngineFrictionJoint2DArray',
   'UnityEngineFrictionJoint2DRef',
   'UnityEngineFrustumPlanes',
   'UnityEngineGameObject',
   'UnityEngineGameObjectArray',
   'UnityEngineGameObjectRef',
   'UnityEngineGradient',
   'UnityEngineGyroscope',
   'UnityEngineHideFlags',
   'UnityEngineHingeJoint',
   'UnityEngineHingeJoint2D',
   'UnityEngineHingeJoint2DArray',
   'UnityEngineHingeJoint2DRef',
   'UnityEngineHingeJointArray',
   'UnityEngineHingeJointRef',
   'UnityEngineHorizontalWrapMode',
   'UnityEngineHumanBodyBones',
   'UnityEngineHumanBone',
   'UnityEngineHumanBoneArray',
   'UnityEngineHumanBoneRef',
   'UnityEngineHumanDescription',
   'UnityEngineHumanDescriptionArray',
   'UnityEngineHumanDescriptionRef',
   'UnityEngineHumanLimit',
   'UnityEngineHumanLimitArray',
   'UnityEngineHumanLimitRef',
   'UnityEngineHumanPartDof',
   'UnityEngineHumanPose',
   'UnityEngineHumanPoseArray',
   'UnityEngineHumanPoseHandler',
   'UnityEngineHumanPoseHandlerArray',
   'UnityEngineHumanPoseHandlerRef',
   'UnityEngineHumanPoseRef',
   'UnityEngineHumanTrait',
   'UnityEngineHumanTraitArray',
  'UnityEngineHumanTraitRef',
   'UnityEngineILogger',
   'UnityEngineIMECompositionMode',
   'UnityEngineInput',
   'UnityEngineInputArray',
   'UnityEngineInputRef',
   'UnityEngineJoint',
   'UnityEngineJoint2D',
   'UnityEngineJoint2DArray',
   'UnityEngineJoint2DRef',
   'UnityEngineJointAngleLimits2D',
   'UnityEngineJointArray',
   'UnityEngineJointDrive',
   'UnityEngineJointLimitState2D',
   'UnityEngineJointLimits',
   'UnityEngineJointMotor',
   'UnityEngineJointMotor2D',
   'UnityEngineJointProjectionMode',
   'UnityEngineJointRef',
   'UnityEngineJointSpring',
   'UnityEngineJointSuspension2D',
   'UnityEngineJointTranslationLimits2D',
   'UnityEngineKeyCode',
   'UnityEngineLayerMask',
   'UnityEngineLayerMaskArray',
   'UnityEngineLayerMaskRef',
   'UnityEngineLight',
   'UnityEngineLightArray',
   'UnityEngineLightBakingOutput',
   'UnityEngineLightRef',
   'UnityEngineLightRenderMode',
   'UnityEngineLightShadowCasterMode',
   'UnityEngineLightShadows',
   'UnityEngineLightType',
   'UnityEngineLineAlignment',
   'UnityEngineLineRenderer',
   'UnityEngineLineRendererArray',
   'UnityEngineLineRendererRef',
   'UnityEngineLineTextureMode',
   'UnityEngineLocationService',
   'UnityEngineMatchTargetWeightMask',
   'UnityEngineMatchTargetWeightMaskArray',
   'UnityEngineMatchTargetWeightMaskRef',
   'UnityEngineMaterial',
   'UnityEngineMaterialArray',
   'UnityEngineMaterialGlobalIlluminationFlags',
   'UnityEngineMaterialPropertyBlock',
   'UnityEngineMaterialPropertyBlockArray',
   'UnityEngineMaterialPropertyBlockRef',
   'UnityEngineMaterialRef',
   'UnityEngineMathf',
   'UnityEngineMathfArray',
   'UnityEngineMathfRef',
   'UnityEngineMatrix4x4',
   'UnityEngineMatrix4x4Array',
   'UnityEngineMatrix4x4Ref',
   'UnityEngineMesh',
   'UnityEngineMeshArray',
   'UnityEngineMeshCollider',
   'UnityEngineMeshColliderArray',
   'UnityEngineMeshColliderCookingOptions',
   'UnityEngineMeshColliderRef',
   'UnityEngineMeshFilter',
   'UnityEngineMeshFilterArray',
   'UnityEngineMeshFilterRef',
   'UnityEngineMeshRef',
   'UnityEngineMeshRenderer',
   'UnityEngineMeshRendererArray',
   'UnityEngineMeshRendererRef',
   'UnityEngineMeshTopology',
   'UnityEngineMotion',
   'UnityEngineMotionArray',
   'UnityEngineMotionRef',
   'UnityEngineMotionVectorGenerationMode',
   'UnityEngineObject',
   'UnityEngineObjectArray',
   'UnityEngineObjectRef',
   'UnityEngineParticleSystem',
   'UnityEngineParticleSystemAnimationMode',
   'UnityEngineParticleSystemAnimationTimeMode',
   'UnityEngineParticleSystemAnimationType',
   'UnityEngineParticleSystemArray',
   'UnityEngineParticleSystemBurst',
   'UnityEngineParticleSystemBurstArray',
   'UnityEngineParticleSystemBurstRef',
   'UnityEngineParticleSystemCollisionMode',
   'UnityEngineParticleSystemCollisionModule',
   'UnityEngineParticleSystemCollisionModuleArray',
   'UnityEngineParticleSystemCollisionModuleRef',
   'UnityEngineParticleSystemCollisionQuality',
   'UnityEngineParticleSystemCollisionType',
   'UnityEngineParticleSystemColorBySpeedModule',
   'UnityEngineParticleSystemColorBySpeedModuleArray',
   'UnityEngineParticleSystemColorBySpeedModuleRef',
   'UnityEngineParticleSystemColorOverLifetimeModule',
   'UnityEngineParticleSystemCullingMode',
   'UnityEngineParticleSystemCurveMode',
   'UnityEngineParticleSystemCustomData',
   'UnityEngineParticleSystemCustomDataMode',
   'UnityEngineParticleSystemCustomDataModule',
   'UnityEngineParticleSystemCustomDataModuleArray',
   'UnityEngineParticleSystemCustomDataModuleRef',
   'UnityEngineParticleSystemEmissionModule',
   'UnityEngineParticleSystemEmissionModuleArray',
   'UnityEngineParticleSystemEmissionModuleRef',
   'UnityEngineParticleSystemEmitParams',
   'UnityEngineParticleSystemEmitParamsArray',
   'UnityEngineParticleSystemEmitParamsRef',
   'UnityEngineParticleSystemEmitterVelocityMode',
   'UnityEngineParticleSystemExternalForcesModule',
   'UnityEngineParticleSystemExternalForcesModuleArray',
   'UnityEngineParticleSystemExternalForcesModuleRef',
   'UnityEngineParticleSystemForceField',
   'UnityEngineParticleSystemForceOverLifetimeModule',
   'UnityEngineParticleSystemForceOverLifetimeModuleArray',
   'UnityEngineParticleSystemForceOverLifetimeModuleRef',
   'UnityEngineParticleSystemGameObjectFilter',
   'UnityEngineParticleSystemGradientMode',
   'UnityEngineParticleSystemInheritVelocityMode',
   'UnityEngineParticleSystemInheritVelocityModule',
   'UnityEngineParticleSystemInheritVelocityModuleArray',
   'UnityEngineParticleSystemInheritVelocityModuleRef',
   'UnityEngineParticleSystemLightsModule',
   'UnityEngineParticleSystemLightsModuleArray',
   'UnityEngineParticleSystemLightsModuleRef',
   'UnityEngineParticleSystemLimitVelocityOverLifetimeModule',
   'UnityEngineParticleSystemLimitVelocityOverLifetimeModuleArray',
   'UnityEngineParticleSystemLimitVelocityOverLifetimeModuleRef',
   'UnityEngineParticleSystemMainModule',
   'UnityEngineParticleSystemMainModuleArray',
   'UnityEngineParticleSystemMainModuleRef',
   'UnityEngineParticleSystemMeshShapeType',
   'UnityEngineParticleSystemMinMaxCurve',
   'UnityEngineParticleSystemMinMaxCurveArray',
   'UnityEngineParticleSystemMinMaxCurveRef',
   'UnityEngineParticleSystemMinMaxGradient',
   'UnityEngineParticleSystemMinMaxGradientArray',
   'UnityEngineParticleSystemMinMaxGradientRef',
   'UnityEngineParticleSystemNoiseModule',
   'UnityEngineParticleSystemNoiseModuleArray',
   'UnityEngineParticleSystemNoiseModuleRef',
   'UnityEngineParticleSystemNoiseQuality',
   'UnityEngineParticleSystemOverlapAction',
   'UnityEngineParticleSystemParticle',
   'UnityEngineParticleSystemParticleArray',
   'UnityEngineParticleSystemParticleRef',
   'UnityEngineParticleSystemRef',
   'UnityEngineParticleSystemRingBufferMode',
   'UnityEngineParticleSystemRotationBySpeedModule',
   'UnityEngineParticleSystemRotationBySpeedModuleArray',
   'UnityEngineParticleSystemRotationBySpeedModuleRef',
   'UnityEngineParticleSystemRotationOverLifetimeModule',
   'UnityEngineParticleSystemRotationOverLifetimeModuleArray',
   'UnityEngineParticleSystemRotationOverLifetimeModuleRef',
   'UnityEngineParticleSystemScalingMode',
  'UnityEngineParticleSystemShapeModule',
   'UnityEngineParticleSystemShapeModuleArray',
   'UnityEngineParticleSystemShapeModuleRef',
   'UnityEngineParticleSystemShapeMultiModeValue',
   'UnityEngineParticleSystemShapeTextureChannel',
   'UnityEngineParticleSystemShapeType',
   'UnityEngineParticleSystemSimulationSpace',
   'UnityEngineParticleSystemSizeBySpeedModule',
   'UnityEngineParticleSystemSizeBySpeedModuleArray',
   'UnityEngineParticleSystemSizeBySpeedModuleRef',
   'UnityEngineParticleSystemSizeOverLifetimeModule',
   'UnityEngineParticleSystemSizeOverLifetimeModuleArray',
   'UnityEngineParticleSystemSizeOverLifetimeModuleRef',
   'UnityEngineParticleSystemStopAction',
   'UnityEngineParticleSystemStopBehavior',
   'UnityEngineParticleSystemSubEmitterProperties',
   'UnityEngineParticleSystemSubEmitterType',
   'UnityEngineParticleSystemSubEmittersModule',
   'UnityEngineParticleSystemSubEmittersModuleArray',
   'UnityEngineParticleSystemSubEmittersModuleRef',
   'UnityEngineParticleSystemTextureSheetAnimationModule',
   'UnityEngineParticleSystemTextureSheetAnimationModuleArray',
   'UnityEngineParticleSystemTextureSheetAnimationModuleRef',
   'UnityEngineParticleSystemTrailMode',
   'UnityEngineParticleSystemTrailModule',
   'UnityEngineParticleSystemTrailModuleArray',
   'UnityEngineParticleSystemTrailModuleRef',
   'UnityEngineParticleSystemTrailTextureMode',
   'UnityEngineParticleSystemTriggerModule',
   'UnityEngineParticleSystemTriggerModuleArray',
   'UnityEngineParticleSystemTriggerModuleRef',
   'UnityEngineParticleSystemVelocityOverLifetimeModule',
   'UnityEngineParticleSystemVelocityOverLifetimeModuleArray',
   'UnityEngineParticleSystemVelocityOverLifetimeModuleRef',
   'UnityEnginePhysicMaterial',
   'UnityEnginePhysicMaterialArray',
   'UnityEnginePhysicMaterialCombine',
   'UnityEnginePhysicMaterialRef',
   'UnityEnginePhysics',
   'UnityEnginePhysics2D',
   'UnityEnginePhysics2DArray',
   'UnityEnginePhysics2DRef',
   'UnityEnginePhysicsArray',
   'UnityEnginePhysicsJobOptions2D',
   'UnityEnginePhysicsMaterial2D',
   'UnityEnginePhysicsMaterial2DArray',
   'UnityEnginePhysicsMaterial2DRef',
   'UnityEnginePhysicsRef',
   'UnityEnginePhysicsScene',
   'UnityEnginePhysicsScene2D',
   'UnityEnginePlane',
   'UnityEnginePlatformEffector2D',
   'UnityEnginePlatformEffector2DArray',
   'UnityEnginePlatformEffector2DRef',
   'UnityEnginePlayMode',
   'UnityEnginePlayablesPlayableGraph',
   'UnityEnginePointEffector2D',
   'UnityEnginePointEffector2DArray',
   'UnityEnginePointEffector2DRef',
   'UnityEnginePolygonCollider2D',
   'UnityEnginePolygonCollider2DArray',
   'UnityEnginePolygonCollider2DRef',
   'UnityEnginePrimitiveType',
   'UnityEngineQualitySettings',
   'UnityEngineQualitySettingsArray',
   'UnityEngineQualitySettingsRef',
   'UnityEngineQuaternion',
   'UnityEngineQuaternionArray',
   'UnityEngineQuaternionRef',
   'UnityEngineQueryTriggerInteraction',
   'UnityEngineQueueMode',
   'UnityEngineRandom',
   'UnityEngineRandomArray',
   'UnityEngineRandomRef',
   'UnityEngineRandomState',
   'UnityEngineRay',
   'UnityEngineRayArray',
   'UnityEngineRayRef',
   'UnityEngineRaycastHit',
   'UnityEngineRaycastHit2D',
   'UnityEngineRaycastHit2DArray',
   'UnityEngineRaycastHit2DRef',
   'UnityEngineRaycastHitArray',
   'UnityEngineRaycastHitRef',
   'UnityEngineRect',
   'UnityEngineRectOffset',
   'UnityEngineRectTransform',
   'UnityEngineRectTransformArray',
   'UnityEngineRectTransformAxis',
   'UnityEngineRectTransformEdge',
   'UnityEngineRectTransformReapplyDrivenProperties',
   'UnityEngineRectTransformRef',
   'UnityEngineRelativeJoint2D',
   'UnityEngineRelativeJoint2DArray',
   'UnityEngineRelativeJoint2DRef',
   'UnityEngineRenderBuffer',
   'UnityEngineRenderBufferArray',
   'UnityEngineRenderMode',
   'UnityEngineRenderSettings',
   'UnityEngineRenderSettingsArray',
   'UnityEngineRenderSettingsRef',
   'UnityEngineRenderTexture',
   'UnityEngineRenderer',
   'UnityEngineRendererArray',
   'UnityEngineRendererExtensions',
   'UnityEngineRendererRef',
   'UnityEngineRenderingAmbientMode',
   'UnityEngineRenderingCameraEvent',
   'UnityEngineRenderingCommandBuffer',
   'UnityEngineRenderingCommandBufferArray',
   'UnityEngineRenderingComputeQueueType',
   'UnityEngineRenderingIndexFormat',
   'UnityEngineRenderingLightEvent',
   'UnityEngineRenderingLightProbeUsage',
   'UnityEngineRenderingLightShadowResolution',
   'UnityEngineRenderingOpaqueSortMode',
   'UnityEngineRenderingPath',
   'UnityEngineRenderingShadowCastingMode',
   'UnityEngineRenderingShadowMapPass',
   'UnityEngineRenderingSphericalHarmonicsL2',
   'UnityEngineRenderingSphericalHarmonicsL2Array',
   'UnityEngineRenderingUVChannelFlags',
   'UnityEngineRigidbody',
   'UnityEngineRigidbody2D',
   'UnityEngineRigidbody2DArray',
   'UnityEngineRigidbody2DRef',
   'UnityEngineRigidbodyArray',
   'UnityEngineRigidbodyConstraints',
   'UnityEngineRigidbodyConstraints2D',
   'UnityEngineRigidbodyInterpolation',
   'UnityEngineRigidbodyInterpolation2D',
   'UnityEngineRigidbodyRef',
   'UnityEngineRigidbodySleepMode2D',
   'UnityEngineRigidbodyType2D',
   'UnityEngineRotationDriveMode',
   'UnityEngineRuntimeAnimatorController',
   'UnityEngineRuntimeAnimatorControllerArray',
   'UnityEngineRuntimeAnimatorControllerRef',
   'UnityEngineSceneManagementScene',
   'UnityEngineScriptableObject',
   'UnityEngineSendMessageOptions',
   'UnityEngineShader',
   'UnityEngineShadowProjection',
   'UnityEngineShadowQuality',
   'UnityEngineShadowResolution',
   'UnityEngineShadowmaskMode',
  'UnityEngineSkeletonBone',
   'UnityEngineSkeletonBoneArray',
   'UnityEngineSkeletonBoneRef',
   'UnityEngineSkinQuality',
   'UnityEngineSkinnedMeshRenderer',
   'UnityEngineSkinnedMeshRendererArray',
   'UnityEngineSkinnedMeshRendererRef',
   'UnityEngineSliderJoint2D',
   'UnityEngineSliderJoint2DArray',
   'UnityEngineSliderJoint2DRef',
   'UnityEngineSoftJointLimit',
#   'UnityEngineSoftJointLimitSpring',
#   'UnityEngineSpace',
#   'UnityEngineSphereCollider',
#   'UnityEngineSphereColliderArray',
#   'UnityEngineSphereColliderRef',
#   'UnityEngineSpringJoint',
#   'UnityEngineSpringJointArray',
#   'UnityEngineSpringJointRef',
#   'UnityEngineSprite',
#   'UnityEngineSpriteDrawMode',
#   'UnityEngineSpriteMaskInteraction',
#   'UnityEngineSpriteRenderer',
#   'UnityEngineSpriteRendererArray',
#   'UnityEngineSpriteRendererRef',
#   'UnityEngineSpriteSortPoint',
#   'UnityEngineSpriteTileMode',
#   'UnityEngineStateMachineBehaviourArray',
#   'UnityEngineStereoTargetEyeMask',
#   'UnityEngineSurfaceEffector2D',
#   'UnityEngineSurfaceEffector2DArray',
#   'UnityEngineSurfaceEffector2DRef',
#   'UnityEngineTargetJoint2D',
#   'UnityEngineTargetJoint2DArray',
#   'UnityEngineTargetJoint2DRef',
#   'UnityEngineTextAnchor',
#   'UnityEngineTextAsset',
#   'UnityEngineTextAssetArray',
#   'UnityEngineTextAssetRef',
#   'UnityEngineTextGenerationSettings',
#   'UnityEngineTextGenerator',
#   'UnityEngineTexture',
#   'UnityEngineTexture2D',
#   'UnityEngineTime',
#   'UnityEngineTimeArray',
#   'UnityEngineTimeRef',
#   'UnityEngineTouch',
#   'UnityEngineTouchArray',
#   'UnityEngineTouchScreenKeyboard',
#   'UnityEngineTouchScreenKeyboardType',
#   'UnityEngineTrailRenderer',
#   'UnityEngineTrailRendererArray',
#   'UnityEngineTrailRendererRef',
#   'UnityEngineTransform',
#   'UnityEngineTransformArray',
#   'UnityEngineTransformRef',
#   'UnityEngineTransparencySortMode',
#   'UnityEngineUIAnimationTriggers',
#   'UnityEngineUIAnimationTriggersArray',
#   'UnityEngineUIAnimationTriggersRef',
#   'UnityEngineUIAspectRatioFitter',
#   'UnityEngineUIAspectRatioFitterArray',
#   'UnityEngineUIAspectRatioFitterAspectMode',
#   'UnityEngineUIAspectRatioFitterRef',
#   'UnityEngineUIBaseMeshEffect',
#   'UnityEngineUIBaseMeshEffectArray',
#   'UnityEngineUIBaseMeshEffectRef',
#   'UnityEngineUIButton',
#   'UnityEngineUIButtonArray',
#   'UnityEngineUIButtonButtonClickedEvent',
#   'UnityEngineUIButtonButtonClickedEventArray',
#   'UnityEngineUIButtonButtonClickedEventRef',
#   'UnityEngineUIButtonRef',
#   'UnityEngineUICanvasScaler',
#   'UnityEngineUICanvasScalerArray',
#   'UnityEngineUICanvasScalerRef',
#   'UnityEngineUICanvasScalerScaleMode',
#   'UnityEngineUICanvasScalerScreenMatchMode',
#   'UnityEngineUICanvasScalerUnit',
#   'UnityEngineUICanvasUpdate',
#   'UnityEngineUIClipping',
#   'UnityEngineUIColorBlock',
#   'UnityEngineUIColorBlockArray',
#   'UnityEngineUIColorBlockRef',
#   'UnityEngineUIContentSizeFitter',
#   'UnityEngineUIContentSizeFitterArray',
#   'UnityEngineUIContentSizeFitterFitMode',
#   'UnityEngineUIContentSizeFitterRef',
#   'UnityEngineUIDefaultControls',
#   'UnityEngineUIDefaultControlsResources',
#   'UnityEngineUIDefaultControlsResourcesArray',
#   'UnityEngineUIDefaultControlsResourcesRef',
#   'UnityEngineUIDropdown',
#   'UnityEngineUIDropdownArray',
#   'UnityEngineUIDropdownDropdownEvent',
#   'UnityEngineUIDropdownDropdownEventArray',
#   'UnityEngineUIDropdownDropdownEventRef',
#   'UnityEngineUIDropdownOptionData',
#   'UnityEngineUIDropdownOptionDataArray',
#   'UnityEngineUIDropdownOptionDataList',
#   'UnityEngineUIDropdownOptionDataListArray',
#   'UnityEngineUIDropdownOptionDataListRef',
#   'UnityEngineUIDropdownOptionDataRef',
#   'UnityEngineUIDropdownRef',
#   'UnityEngineUIFontData',
#   'UnityEngineUIFontDataArray',
#   'UnityEngineUIFontDataRef',
#   'UnityEngineUIGraphic',
#   'UnityEngineUIGraphicArray',
#   'UnityEngineUIGraphicRaycaster',
#   'UnityEngineUIGraphicRaycasterArray',
#   'UnityEngineUIGraphicRaycasterBlockingObjects',
#   'UnityEngineUIGraphicRaycasterRef',
#   'UnityEngineUIGraphicRef',
#   'UnityEngineUIGridLayoutGroup',
#   'UnityEngineUIGridLayoutGroupArray',
#   'UnityEngineUIGridLayoutGroupAxis',
#   'UnityEngineUIGridLayoutGroupConstraint',
#   'UnityEngineUIGridLayoutGroupCorner',
#   'UnityEngineUIGridLayoutGroupRef',
#   'UnityEngineUIHorizontalLayoutGroup',
#   'UnityEngineUIHorizontalLayoutGroupArray',
#   'UnityEngineUIHorizontalLayoutGroupRef',
#   'UnityEngineUIHorizontalOrVerticalLayoutGroup',
#   'UnityEngineUIHorizontalOrVerticalLayoutGroupArray',
#   'UnityEngineUIHorizontalOrVerticalLayoutGroupRef',
#   'UnityEngineUIIClippable',
#   'UnityEngineUIILayoutElementRef',
#   'UnityEngineUIImage',
#   'UnityEngineUIImageArray',
#   'UnityEngineUIImageFillMethod',
#   'UnityEngineUIImageRef',
#   'UnityEngineUIImageType',
#   'UnityEngineUIInputField',
#   'UnityEngineUIInputFieldArray',
#   'UnityEngineUIInputFieldCharacterValidation',
#   'UnityEngineUIInputFieldContentType',
#   'UnityEngineUIInputFieldInputType',
#   'UnityEngineUIInputFieldLineType',
#   'UnityEngineUIInputFieldOnChangeEvent',
#   'UnityEngineUIInputFieldOnChangeEventArray',
#   'UnityEngineUIInputFieldOnChangeEventRef',
#   'UnityEngineUIInputFieldOnValidateInput',
#   'UnityEngineUIInputFieldRef',
#   'UnityEngineUIInputFieldSubmitEvent',
#   'UnityEngineUIInputFieldSubmitEventArray',
#   'UnityEngineUIInputFieldSubmitEventRef',
#   'UnityEngineUILayoutElement',
#   'UnityEngineUILayoutElementArray',
#   'UnityEngineUILayoutElementRef',
#   'UnityEngineUILayoutGroup',
#   'UnityEngineUILayoutGroupArray',
#   'UnityEngineUILayoutGroupRef',
#   'UnityEngineUILayoutRebuilder',
#   'UnityEngineUILayoutRebuilderArray',
#   'UnityEngineUILayoutRebuilderRef',
#   'UnityEngineUILayoutUtility',
#   'UnityEngineUIMask',
#   'UnityEngineUIMaskArray',
#   'UnityEngineUIMaskRef',
#   'UnityEngineUIMaskUtilities',
#   'UnityEngineUIMaskUtilitiesArray',
#   'UnityEngineUIMaskUtilitiesRef',
#   'UnityEngineUIMaskableGraphic',
#   'UnityEngineUIMaskableGraphicArray',
#   'UnityEngineUIMaskableGraphicCullStateChangedEvent',
#   'UnityEngineUIMaskableGraphicRef',
#   'UnityEngineUINavigation',
#   'UnityEngineUINavigationArray',
#   'UnityEngineUINavigationMode',
#   'UnityEngineUINavigationRef',
#   'UnityEngineUIOutline',
#   'UnityEngineUIOutlineArray',
#   'UnityEngineUIOutlineRef',
#   'UnityEngineUIPositionAsUV1',
#   'UnityEngineUIPositionAsUV1Array',
#   'UnityEngineUIPositionAsUV1Ref',
#   'UnityEngineUIRawImage',
#   'UnityEngineUIRawImageArray',
#   'UnityEngineUIRawImageRef',
#   'UnityEngineUIRectMask2D',
#   'UnityEngineUIRectMask2DArray',
#   'UnityEngineUIRectMask2DRef',
#   'UnityEngineUIScrollRect',
#   'UnityEngineUIScrollRectArray',
#   'UnityEngineUIScrollRectMovementType',
#   'UnityEngineUIScrollRectRef',
#   'UnityEngineUIScrollRectScrollRectEvent',
#   'UnityEngineUIScrollRectScrollRectEventArray',
#   'UnityEngineUIScrollRectScrollRectEventRef',
#   'UnityEngineUIScrollRectScrollbarVisibility',
#   'UnityEngineUIScrollbar',
#   'UnityEngineUIScrollbarArray',
#   'UnityEngineUIScrollbarDirection',
#   'UnityEngineUIScrollbarRef',
#   'UnityEngineUIScrollbarScrollEvent',
#   'UnityEngineUIScrollbarScrollEventArray',
#   'UnityEngineUIScrollbarScrollEventRef',
#   'UnityEngineUISelectable',
#   'UnityEngineUISelectableArray',
#   'UnityEngineUISelectableRef',
#   'UnityEngineUISelectableTransition',
#   'UnityEngineUIShadow',
#   'UnityEngineUIShadowArray',
#   'UnityEngineUIShadowRef',
#   'UnityEngineUISlider',
#   'UnityEngineUISliderArray',
#   'UnityEngineUISliderDirection',
#   'UnityEngineUISliderRef',
#   'UnityEngineUISliderSliderEvent',
#   'UnityEngineUISliderSliderEventArray',
#   'UnityEngineUISliderSliderEventRef',
#   'UnityEngineUISpriteState',
#   'UnityEngineUISpriteStateArray',
#   'UnityEngineUISpriteStateRef',
#   'UnityEngineUIText',
#   'UnityEngineUITextArray',
#   'UnityEngineUITextRef',
#   'UnityEngineUIToggle',
#   'UnityEngineUIToggleArray',
#   'UnityEngineUIToggleGroup',
#   'UnityEngineUIToggleGroupArray',
#   'UnityEngineUIToggleGroupRef',
#   'UnityEngineUIToggleRef',
#   'UnityEngineUIToggleToggleEvent',
#   'UnityEngineUIToggleToggleEventArray',
#   'UnityEngineUIToggleToggleEventRef',
#   'UnityEngineUIVertex',
#   'UnityEngineUIVertexArray',
#   'UnityEngineUIVertexHelper',
#   'UnityEngineUIVertexHelperArray',
#   'UnityEngineUIVertexHelperRef',
#   'UnityEngineUIVertexRef',
#   'UnityEngineUIVerticalLayoutGroup',
#   'UnityEngineUIVerticalLayoutGroupArray',
#   'UnityEngineUIVerticalLayoutGroupRef',
#   'UnityEngineVector2',
#   'UnityEngineVector2Array',
#   'UnityEngineVector2Ref',
#   'UnityEngineVector3',
#   'UnityEngineVector3Array',
#   'UnityEngineVector3ArrayRef',
#   'UnityEngineVector3Ref',
#   'UnityEngineVector4',
#   'UnityEngineVector4Array',
#   'UnityEngineVector4Ref',
#   'UnityEngineVerticalWrapMode',
#   'UnityEngineWheelCollider',
#   'UnityEngineWheelColliderArray',
#   'UnityEngineWheelColliderRef',
#   'UnityEngineWheelFrictionCurve',
#   'UnityEngineWheelHitRef',
#   'UnityEngineWheelJoint2D',
#   'UnityEngineWheelJoint2DArray',
#   'UnityEngineWheelJoint2DRef',
#   'UnityEngineWrapMode',
#   'VRCSDK3ComponentsVRCAudioBank',
#   'VRCSDK3ComponentsVRCAudioBankArray',
#   'VRCSDK3ComponentsVRCAudioBankRef',
#   'VRCSDK3ComponentsVRCAvatarPedestal',
#   'VRCSDK3ComponentsVRCAvatarPedestalArray',
#   'VRCSDK3ComponentsVRCAvatarPedestalRef',
#   'VRCSDK3ComponentsVRCCombatSystem',
#   'VRCSDK3ComponentsVRCCombatSystemArray',
#   'VRCSDK3ComponentsVRCCombatSystemRef',
#   'VRCSDK3ComponentsVRCObjectSync',
#   'VRCSDK3ComponentsVRCObjectSyncArray',
#   'VRCSDK3ComponentsVRCObjectSyncRef',
#   'VRCSDK3ComponentsVRCPickup',
#   'VRCSDK3ComponentsVRCPickupArray',
#   'VRCSDK3ComponentsVRCPickupRef',
#   'VRCSDK3ComponentsVRCPortalMarker',
#   'VRCSDK3ComponentsVRCPortalMarkerArray',
#   'VRCSDK3ComponentsVRCPortalMarkerRef',
#   'VRCSDK3ComponentsVRCStation',
#   'VRCSDK3ComponentsVRCStationApi',
#   'VRCSDK3ComponentsVRCStationApiArray',
#   'VRCSDK3ComponentsVRCStationApiRef',
#   'VRCSDK3ComponentsVRCStationArray',
#   'VRCSDK3ComponentsVRCStationInput',
#   'VRCSDK3ComponentsVRCStationInputArray',
#   'VRCSDK3ComponentsVRCStationInputRef',
#   'VRCSDK3ComponentsVRCStationRef',
#   'VRCSDKBaseInputManager',
#   'VRCSDKBaseInputManagerArray',
#   'VRCSDKBaseInputManagerRef',
#   'VRCSDKBaseNetworking',
#   'VRCSDKBaseVRCInputMethod',
#   'VRCSDKBaseVRCInputSetting',
#   'VRCSDKBaseVRCPlayerApi',
#   'VRCSDKBaseVRCPlayerApiArray',
#   'VRCSDKBaseVRCPlayerApiRef',
#   'VRCSDKBaseVRCPlayerApiTrackingData',
#   'VRCSDKBaseVRCPlayerApiTrackingDataArray',
#   'VRCSDKBaseVRCPlayerApiTrackingDataRef',
#   'VRCSDKBaseVRCPlayerApiTrackingDataType',
#   'VRCSDKBaseVRC_EventDispatcher',
#   'VRCSDKBaseVRC_EventHandler',
#   'VRCSDKBaseVRC_EventHandlerVrcBroadcastType',
#   'VRCSDKBaseVRC_EventHandlerVrcTargetType',
#   'VRCSDKBaseVRC_Pickup',
#   'VRCSDKBaseVRC_PickupPickupHand',
   # 'VRCSDKBaseVRC_SceneDescriptorSpawnOrientation',
   'VRCUdonCommonInterfacesIUdonEventReceiver',
    'VRCUdonCommonInterfacesNetworkEventTarget'
 ]