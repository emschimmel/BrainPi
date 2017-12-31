/**
 * Autogenerated by Thrift Compiler (0.10.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package nl.earpi.generated.shortmemory;

@SuppressWarnings({"cast", "rawtypes", "serial", "unchecked", "unused"})
@javax.annotation.Generated(value = "Autogenerated by Thrift Compiler (0.10.0)", date = "2017-12-30")
public class DeviceTokenInput implements org.apache.thrift.TBase<DeviceTokenInput, DeviceTokenInput._Fields>, java.io.Serializable, Cloneable, Comparable<DeviceTokenInput> {
  private static final org.apache.thrift.protocol.TStruct STRUCT_DESC = new org.apache.thrift.protocol.TStruct("DeviceTokenInput");

  private static final org.apache.thrift.protocol.TField IP_FIELD_DESC = new org.apache.thrift.protocol.TField("ip", org.apache.thrift.protocol.TType.STRING, (short)1);
  private static final org.apache.thrift.protocol.TField DEVICETYPE_FIELD_DESC = new org.apache.thrift.protocol.TField("devicetype", org.apache.thrift.protocol.TType.STRING, (short)2);
  private static final org.apache.thrift.protocol.TField USER_AGENT_FIELD_DESC = new org.apache.thrift.protocol.TField("userAgent", org.apache.thrift.protocol.TType.STRING, (short)3);
  private static final org.apache.thrift.protocol.TField PERSON_FIELD_DESC = new org.apache.thrift.protocol.TField("person", org.apache.thrift.protocol.TType.STRING, (short)4);

  private static final org.apache.thrift.scheme.SchemeFactory STANDARD_SCHEME_FACTORY = new DeviceTokenInputStandardSchemeFactory();
  private static final org.apache.thrift.scheme.SchemeFactory TUPLE_SCHEME_FACTORY = new DeviceTokenInputTupleSchemeFactory();

  public java.lang.String ip; // required
  public java.lang.String devicetype; // required
  public java.lang.String userAgent; // optional
  public java.lang.String person; // optional

  /** The set of fields this struct contains, along with convenience methods for finding and manipulating them. */
  public enum _Fields implements org.apache.thrift.TFieldIdEnum {
    IP((short)1, "ip"),
    DEVICETYPE((short)2, "devicetype"),
    USER_AGENT((short)3, "userAgent"),
    PERSON((short)4, "person");

    private static final java.util.Map<java.lang.String, _Fields> byName = new java.util.HashMap<java.lang.String, _Fields>();

    static {
      for (_Fields field : java.util.EnumSet.allOf(_Fields.class)) {
        byName.put(field.getFieldName(), field);
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, or null if its not found.
     */
    public static _Fields findByThriftId(int fieldId) {
      switch(fieldId) {
        case 1: // IP
          return IP;
        case 2: // DEVICETYPE
          return DEVICETYPE;
        case 3: // USER_AGENT
          return USER_AGENT;
        case 4: // PERSON
          return PERSON;
        default:
          return null;
      }
    }

    /**
     * Find the _Fields constant that matches fieldId, throwing an exception
     * if it is not found.
     */
    public static _Fields findByThriftIdOrThrow(int fieldId) {
      _Fields fields = findByThriftId(fieldId);
      if (fields == null) throw new java.lang.IllegalArgumentException("Field " + fieldId + " doesn't exist!");
      return fields;
    }

    /**
     * Find the _Fields constant that matches name, or null if its not found.
     */
    public static _Fields findByName(java.lang.String name) {
      return byName.get(name);
    }

    private final short _thriftId;
    private final java.lang.String _fieldName;

    _Fields(short thriftId, java.lang.String fieldName) {
      _thriftId = thriftId;
      _fieldName = fieldName;
    }

    public short getThriftFieldId() {
      return _thriftId;
    }

    public java.lang.String getFieldName() {
      return _fieldName;
    }
  }

  // isset id assignments
  private static final _Fields optionals[] = {_Fields.USER_AGENT,_Fields.PERSON};
  public static final java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> metaDataMap;
  static {
    java.util.Map<_Fields, org.apache.thrift.meta_data.FieldMetaData> tmpMap = new java.util.EnumMap<_Fields, org.apache.thrift.meta_data.FieldMetaData>(_Fields.class);
    tmpMap.put(_Fields.IP, new org.apache.thrift.meta_data.FieldMetaData("ip", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.DEVICETYPE, new org.apache.thrift.meta_data.FieldMetaData("devicetype", org.apache.thrift.TFieldRequirementType.REQUIRED, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.USER_AGENT, new org.apache.thrift.meta_data.FieldMetaData("userAgent", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    tmpMap.put(_Fields.PERSON, new org.apache.thrift.meta_data.FieldMetaData("person", org.apache.thrift.TFieldRequirementType.OPTIONAL, 
        new org.apache.thrift.meta_data.FieldValueMetaData(org.apache.thrift.protocol.TType.STRING)));
    metaDataMap = java.util.Collections.unmodifiableMap(tmpMap);
    org.apache.thrift.meta_data.FieldMetaData.addStructMetaDataMap(DeviceTokenInput.class, metaDataMap);
  }

  public DeviceTokenInput() {
  }

  public DeviceTokenInput(
    java.lang.String ip,
    java.lang.String devicetype)
  {
    this();
    this.ip = ip;
    this.devicetype = devicetype;
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public DeviceTokenInput(DeviceTokenInput other) {
    if (other.isSetIp()) {
      this.ip = other.ip;
    }
    if (other.isSetDevicetype()) {
      this.devicetype = other.devicetype;
    }
    if (other.isSetUserAgent()) {
      this.userAgent = other.userAgent;
    }
    if (other.isSetPerson()) {
      this.person = other.person;
    }
  }

  public DeviceTokenInput deepCopy() {
    return new DeviceTokenInput(this);
  }

  @Override
  public void clear() {
    this.ip = null;
    this.devicetype = null;
    this.userAgent = null;
    this.person = null;
  }

  public java.lang.String getIp() {
    return this.ip;
  }

  public DeviceTokenInput setIp(java.lang.String ip) {
    this.ip = ip;
    return this;
  }

  public void unsetIp() {
    this.ip = null;
  }

  /** Returns true if field ip is set (has been assigned a value) and false otherwise */
  public boolean isSetIp() {
    return this.ip != null;
  }

  public void setIpIsSet(boolean value) {
    if (!value) {
      this.ip = null;
    }
  }

  public java.lang.String getDevicetype() {
    return this.devicetype;
  }

  public DeviceTokenInput setDevicetype(java.lang.String devicetype) {
    this.devicetype = devicetype;
    return this;
  }

  public void unsetDevicetype() {
    this.devicetype = null;
  }

  /** Returns true if field devicetype is set (has been assigned a value) and false otherwise */
  public boolean isSetDevicetype() {
    return this.devicetype != null;
  }

  public void setDevicetypeIsSet(boolean value) {
    if (!value) {
      this.devicetype = null;
    }
  }

  public java.lang.String getUserAgent() {
    return this.userAgent;
  }

  public DeviceTokenInput setUserAgent(java.lang.String userAgent) {
    this.userAgent = userAgent;
    return this;
  }

  public void unsetUserAgent() {
    this.userAgent = null;
  }

  /** Returns true if field userAgent is set (has been assigned a value) and false otherwise */
  public boolean isSetUserAgent() {
    return this.userAgent != null;
  }

  public void setUserAgentIsSet(boolean value) {
    if (!value) {
      this.userAgent = null;
    }
  }

  public java.lang.String getPerson() {
    return this.person;
  }

  public DeviceTokenInput setPerson(java.lang.String person) {
    this.person = person;
    return this;
  }

  public void unsetPerson() {
    this.person = null;
  }

  /** Returns true if field person is set (has been assigned a value) and false otherwise */
  public boolean isSetPerson() {
    return this.person != null;
  }

  public void setPersonIsSet(boolean value) {
    if (!value) {
      this.person = null;
    }
  }

  public void setFieldValue(_Fields field, java.lang.Object value) {
    switch (field) {
    case IP:
      if (value == null) {
        unsetIp();
      } else {
        setIp((java.lang.String)value);
      }
      break;

    case DEVICETYPE:
      if (value == null) {
        unsetDevicetype();
      } else {
        setDevicetype((java.lang.String)value);
      }
      break;

    case USER_AGENT:
      if (value == null) {
        unsetUserAgent();
      } else {
        setUserAgent((java.lang.String)value);
      }
      break;

    case PERSON:
      if (value == null) {
        unsetPerson();
      } else {
        setPerson((java.lang.String)value);
      }
      break;

    }
  }

  public java.lang.Object getFieldValue(_Fields field) {
    switch (field) {
    case IP:
      return getIp();

    case DEVICETYPE:
      return getDevicetype();

    case USER_AGENT:
      return getUserAgent();

    case PERSON:
      return getPerson();

    }
    throw new java.lang.IllegalStateException();
  }

  /** Returns true if field corresponding to fieldID is set (has been assigned a value) and false otherwise */
  public boolean isSet(_Fields field) {
    if (field == null) {
      throw new java.lang.IllegalArgumentException();
    }

    switch (field) {
    case IP:
      return isSetIp();
    case DEVICETYPE:
      return isSetDevicetype();
    case USER_AGENT:
      return isSetUserAgent();
    case PERSON:
      return isSetPerson();
    }
    throw new java.lang.IllegalStateException();
  }

  @Override
  public boolean equals(java.lang.Object that) {
    if (that == null)
      return false;
    if (that instanceof DeviceTokenInput)
      return this.equals((DeviceTokenInput)that);
    return false;
  }

  public boolean equals(DeviceTokenInput that) {
    if (that == null)
      return false;
    if (this == that)
      return true;

    boolean this_present_ip = true && this.isSetIp();
    boolean that_present_ip = true && that.isSetIp();
    if (this_present_ip || that_present_ip) {
      if (!(this_present_ip && that_present_ip))
        return false;
      if (!this.ip.equals(that.ip))
        return false;
    }

    boolean this_present_devicetype = true && this.isSetDevicetype();
    boolean that_present_devicetype = true && that.isSetDevicetype();
    if (this_present_devicetype || that_present_devicetype) {
      if (!(this_present_devicetype && that_present_devicetype))
        return false;
      if (!this.devicetype.equals(that.devicetype))
        return false;
    }

    boolean this_present_userAgent = true && this.isSetUserAgent();
    boolean that_present_userAgent = true && that.isSetUserAgent();
    if (this_present_userAgent || that_present_userAgent) {
      if (!(this_present_userAgent && that_present_userAgent))
        return false;
      if (!this.userAgent.equals(that.userAgent))
        return false;
    }

    boolean this_present_person = true && this.isSetPerson();
    boolean that_present_person = true && that.isSetPerson();
    if (this_present_person || that_present_person) {
      if (!(this_present_person && that_present_person))
        return false;
      if (!this.person.equals(that.person))
        return false;
    }

    return true;
  }

  @Override
  public int hashCode() {
    int hashCode = 1;

    hashCode = hashCode * 8191 + ((isSetIp()) ? 131071 : 524287);
    if (isSetIp())
      hashCode = hashCode * 8191 + ip.hashCode();

    hashCode = hashCode * 8191 + ((isSetDevicetype()) ? 131071 : 524287);
    if (isSetDevicetype())
      hashCode = hashCode * 8191 + devicetype.hashCode();

    hashCode = hashCode * 8191 + ((isSetUserAgent()) ? 131071 : 524287);
    if (isSetUserAgent())
      hashCode = hashCode * 8191 + userAgent.hashCode();

    hashCode = hashCode * 8191 + ((isSetPerson()) ? 131071 : 524287);
    if (isSetPerson())
      hashCode = hashCode * 8191 + person.hashCode();

    return hashCode;
  }

  @Override
  public int compareTo(DeviceTokenInput other) {
    if (!getClass().equals(other.getClass())) {
      return getClass().getName().compareTo(other.getClass().getName());
    }

    int lastComparison = 0;

    lastComparison = java.lang.Boolean.valueOf(isSetIp()).compareTo(other.isSetIp());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetIp()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.ip, other.ip);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetDevicetype()).compareTo(other.isSetDevicetype());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetDevicetype()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.devicetype, other.devicetype);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetUserAgent()).compareTo(other.isSetUserAgent());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetUserAgent()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.userAgent, other.userAgent);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    lastComparison = java.lang.Boolean.valueOf(isSetPerson()).compareTo(other.isSetPerson());
    if (lastComparison != 0) {
      return lastComparison;
    }
    if (isSetPerson()) {
      lastComparison = org.apache.thrift.TBaseHelper.compareTo(this.person, other.person);
      if (lastComparison != 0) {
        return lastComparison;
      }
    }
    return 0;
  }

  public _Fields fieldForId(int fieldId) {
    return _Fields.findByThriftId(fieldId);
  }

  public void read(org.apache.thrift.protocol.TProtocol iprot) throws org.apache.thrift.TException {
    scheme(iprot).read(iprot, this);
  }

  public void write(org.apache.thrift.protocol.TProtocol oprot) throws org.apache.thrift.TException {
    scheme(oprot).write(oprot, this);
  }

  @Override
  public java.lang.String toString() {
    java.lang.StringBuilder sb = new java.lang.StringBuilder("DeviceTokenInput(");
    boolean first = true;

    sb.append("ip:");
    if (this.ip == null) {
      sb.append("null");
    } else {
      sb.append(this.ip);
    }
    first = false;
    if (!first) sb.append(", ");
    sb.append("devicetype:");
    if (this.devicetype == null) {
      sb.append("null");
    } else {
      sb.append(this.devicetype);
    }
    first = false;
    if (isSetUserAgent()) {
      if (!first) sb.append(", ");
      sb.append("userAgent:");
      if (this.userAgent == null) {
        sb.append("null");
      } else {
        sb.append(this.userAgent);
      }
      first = false;
    }
    if (isSetPerson()) {
      if (!first) sb.append(", ");
      sb.append("person:");
      if (this.person == null) {
        sb.append("null");
      } else {
        sb.append(this.person);
      }
      first = false;
    }
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws org.apache.thrift.TException {
    // check for required fields
    if (ip == null) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'ip' was not present! Struct: " + toString());
    }
    if (devicetype == null) {
      throw new org.apache.thrift.protocol.TProtocolException("Required field 'devicetype' was not present! Struct: " + toString());
    }
    // check for sub-struct validity
  }

  private void writeObject(java.io.ObjectOutputStream out) throws java.io.IOException {
    try {
      write(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(out)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private void readObject(java.io.ObjectInputStream in) throws java.io.IOException, java.lang.ClassNotFoundException {
    try {
      read(new org.apache.thrift.protocol.TCompactProtocol(new org.apache.thrift.transport.TIOStreamTransport(in)));
    } catch (org.apache.thrift.TException te) {
      throw new java.io.IOException(te);
    }
  }

  private static class DeviceTokenInputStandardSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public DeviceTokenInputStandardScheme getScheme() {
      return new DeviceTokenInputStandardScheme();
    }
  }

  private static class DeviceTokenInputStandardScheme extends org.apache.thrift.scheme.StandardScheme<DeviceTokenInput> {

    public void read(org.apache.thrift.protocol.TProtocol iprot, DeviceTokenInput struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TField schemeField;
      iprot.readStructBegin();
      while (true)
      {
        schemeField = iprot.readFieldBegin();
        if (schemeField.type == org.apache.thrift.protocol.TType.STOP) { 
          break;
        }
        switch (schemeField.id) {
          case 1: // IP
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.ip = iprot.readString();
              struct.setIpIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 2: // DEVICETYPE
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.devicetype = iprot.readString();
              struct.setDevicetypeIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 3: // USER_AGENT
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.userAgent = iprot.readString();
              struct.setUserAgentIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          case 4: // PERSON
            if (schemeField.type == org.apache.thrift.protocol.TType.STRING) {
              struct.person = iprot.readString();
              struct.setPersonIsSet(true);
            } else { 
              org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
            }
            break;
          default:
            org.apache.thrift.protocol.TProtocolUtil.skip(iprot, schemeField.type);
        }
        iprot.readFieldEnd();
      }
      iprot.readStructEnd();

      // check for required fields of primitive type, which can't be checked in the validate method
      struct.validate();
    }

    public void write(org.apache.thrift.protocol.TProtocol oprot, DeviceTokenInput struct) throws org.apache.thrift.TException {
      struct.validate();

      oprot.writeStructBegin(STRUCT_DESC);
      if (struct.ip != null) {
        oprot.writeFieldBegin(IP_FIELD_DESC);
        oprot.writeString(struct.ip);
        oprot.writeFieldEnd();
      }
      if (struct.devicetype != null) {
        oprot.writeFieldBegin(DEVICETYPE_FIELD_DESC);
        oprot.writeString(struct.devicetype);
        oprot.writeFieldEnd();
      }
      if (struct.userAgent != null) {
        if (struct.isSetUserAgent()) {
          oprot.writeFieldBegin(USER_AGENT_FIELD_DESC);
          oprot.writeString(struct.userAgent);
          oprot.writeFieldEnd();
        }
      }
      if (struct.person != null) {
        if (struct.isSetPerson()) {
          oprot.writeFieldBegin(PERSON_FIELD_DESC);
          oprot.writeString(struct.person);
          oprot.writeFieldEnd();
        }
      }
      oprot.writeFieldStop();
      oprot.writeStructEnd();
    }

  }

  private static class DeviceTokenInputTupleSchemeFactory implements org.apache.thrift.scheme.SchemeFactory {
    public DeviceTokenInputTupleScheme getScheme() {
      return new DeviceTokenInputTupleScheme();
    }
  }

  private static class DeviceTokenInputTupleScheme extends org.apache.thrift.scheme.TupleScheme<DeviceTokenInput> {

    @Override
    public void write(org.apache.thrift.protocol.TProtocol prot, DeviceTokenInput struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol oprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      oprot.writeString(struct.ip);
      oprot.writeString(struct.devicetype);
      java.util.BitSet optionals = new java.util.BitSet();
      if (struct.isSetUserAgent()) {
        optionals.set(0);
      }
      if (struct.isSetPerson()) {
        optionals.set(1);
      }
      oprot.writeBitSet(optionals, 2);
      if (struct.isSetUserAgent()) {
        oprot.writeString(struct.userAgent);
      }
      if (struct.isSetPerson()) {
        oprot.writeString(struct.person);
      }
    }

    @Override
    public void read(org.apache.thrift.protocol.TProtocol prot, DeviceTokenInput struct) throws org.apache.thrift.TException {
      org.apache.thrift.protocol.TTupleProtocol iprot = (org.apache.thrift.protocol.TTupleProtocol) prot;
      struct.ip = iprot.readString();
      struct.setIpIsSet(true);
      struct.devicetype = iprot.readString();
      struct.setDevicetypeIsSet(true);
      java.util.BitSet incoming = iprot.readBitSet(2);
      if (incoming.get(0)) {
        struct.userAgent = iprot.readString();
        struct.setUserAgentIsSet(true);
      }
      if (incoming.get(1)) {
        struct.person = iprot.readString();
        struct.setPersonIsSet(true);
      }
    }
  }

  private static <S extends org.apache.thrift.scheme.IScheme> S scheme(org.apache.thrift.protocol.TProtocol proto) {
    return (org.apache.thrift.scheme.StandardScheme.class.equals(proto.getScheme()) ? STANDARD_SCHEME_FACTORY : TUPLE_SCHEME_FACTORY).getScheme();
  }
}

