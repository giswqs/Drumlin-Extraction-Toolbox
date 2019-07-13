__author__ = 'Dr. Qiusheng Wu @ http://wetlands.io'
import arcpy

# main script
if __name__ == '__main__':
    in_fc = arcpy.GetParameterAsText(0)
    out_fc = arcpy.GetParameterAsText(1)
    geometry_type = arcpy.GetParameterAsText(2)
    group_option = arcpy.GetParameterAsText(3)
    group_field = arcpy.GetParameterAsText(4)
    mbg_fields_option = arcpy.GetParameterAsText(5)

    if mbg_fields_option.lower() == "true":
        mbg_fields_option = "MBG_FIELDS"
    else:
        mbg_fields_option = "NO_MBG_FIELDS"

    arcpy.MinimumBoundingGeometry_management(in_fc,out_fc,geometry_type,group_option,group_field,mbg_fields_option)
