__author__ = 'Dr. Qiusheng Wu @ http://wetlands.io'
import arcpy

# main script
if __name__ == '__main__':

    in_raster = arcpy.GetParameterAsText(0)
    out_raster = arcpy.GetParameterAsText(1)
    neighborhood = arcpy.GetParameterAsText(2)
    statistics_type = arcpy.GetParameterAsText(3)
    no_data = arcpy.GetParameterAsText(4)

    ignore_nodata = "DATA"
    if no_data.lower() == "false":
        ignore_nodata = "NODATA"

    tmp_ras = arcpy.sa.FocalStatistics(in_raster,neighborhood,statistics_type,ignore_nodata)
    tmp_ras.save(out_raster)