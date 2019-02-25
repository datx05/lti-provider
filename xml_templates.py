def get_xml_config():
    return """
    <?xml version="1.0" encoding="UTF-8"?>
    <cartridge_basiclti_link xmlns="http://www.imsglobal.org/xsd/imslticc_v1p0"
        xmlns:blti = "http://www.imsglobal.org/xsd/imsbasiclti_v1p0"
        xmlns:lticm ="http://www.imsglobal.org/xsd/imslticm_v1p0"
        xmlns:lticp ="http://www.imsglobal.org/xsd/imslticp_v1p0"
        xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation = "http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0.xsd
        http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0.xsd
        http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd
        http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd">
        <blti:title>Master Thesis</blti:title>
        <blti:description>Assignment checking</blti:description>
        <blti:icon></blti:icon>
        <blti:launch_url>http://canvas-232314.appspot.com/</blti:launch_url>
        <blti:extensions platform="canvas.instructure.com">
          <lticm:property name="tool_id">datx05_jmnt</lticm:property>
          <lticm:property name="privacy_level">name_only</lticm:property>
          <lticm:property name="domain">canvas-232314.appspot.com</lticm:property>
        </blti:extensions>
        <cartridge_bundle identifierref="BLTI001_Bundle"/>
        <cartridge_icon identifierref="BLTI001_Icon"/>
    </cartridge_basiclti_link>  
    """