# generated from dolly_ignition/env-hooks/dolly_ignition.sh.in

ament_prepend_unique_value IGN_GAZEBO_RESOURCE_PATH "$AMENT_CURRENT_PREFIX/share/dolly_ignition/models"
ament_prepend_unique_value IGN_GAZEBO_RESOURCE_PATH "$AMENT_CURRENT_PREFIX/share/dolly_ignition/worlds"

export MESA_GL_VERSION_OVERRIDE=3.3

# Deprecated

ament_prepend_unique_value SDF_PATH "$AMENT_CURRENT_PREFIX/share/dolly_ignition/models"
ament_prepend_unique_value SDF_PATH "$AMENT_CURRENT_PREFIX/share/dolly_ignition/worlds"

ament_prepend_unique_value IGN_FILE_PATH "$AMENT_CURRENT_PREFIX/share/dolly_ignition/models"
ament_prepend_unique_value IGN_FILE_PATH "$AMENT_CURRENT_PREFIX/share/dolly_ignition/worlds"
