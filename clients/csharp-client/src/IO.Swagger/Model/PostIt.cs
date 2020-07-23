/* 
 * Post-it digitalization API
 *
 * Post-it digitalization API
 *
 * OpenAPI spec version: 1.0.0
 * Contact: muellerobin95@gmail.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// PostIt
    /// </summary>
    [DataContract]
        public partial class PostIt :  IEquatable<PostIt>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="PostIt" /> class.
        /// </summary>
        /// <param name="id">id (required).</param>
        /// <param name="contents">contents (required).</param>
        /// <param name="color">color (required).</param>
        /// <param name="coordinates">coordinates (required).</param>
        /// <param name="width">width (required).</param>
        /// <param name="height">height (required).</param>
        public PostIt(Guid? id = default(Guid?), string contents = default(string), string color = default(string), Coordinate coordinates = default(Coordinate), double? width = default(double?), double? height = default(double?))
        {
            // to ensure "id" is required (not null)
            if (id == null)
            {
                throw new InvalidDataException("id is a required property for PostIt and cannot be null");
            }
            else
            {
                this.Id = id;
            }
            // to ensure "contents" is required (not null)
            if (contents == null)
            {
                throw new InvalidDataException("contents is a required property for PostIt and cannot be null");
            }
            else
            {
                this.Contents = contents;
            }
            // to ensure "color" is required (not null)
            if (color == null)
            {
                throw new InvalidDataException("color is a required property for PostIt and cannot be null");
            }
            else
            {
                this.Color = color;
            }
            // to ensure "coordinates" is required (not null)
            if (coordinates == null)
            {
                throw new InvalidDataException("coordinates is a required property for PostIt and cannot be null");
            }
            else
            {
                this.Coordinates = coordinates;
            }
            // to ensure "width" is required (not null)
            if (width == null)
            {
                throw new InvalidDataException("width is a required property for PostIt and cannot be null");
            }
            else
            {
                this.Width = width;
            }
            // to ensure "height" is required (not null)
            if (height == null)
            {
                throw new InvalidDataException("height is a required property for PostIt and cannot be null");
            }
            else
            {
                this.Height = height;
            }
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public Guid? Id { get; set; }

        /// <summary>
        /// Gets or Sets Contents
        /// </summary>
        [DataMember(Name="contents", EmitDefaultValue=false)]
        public string Contents { get; set; }

        /// <summary>
        /// Gets or Sets Color
        /// </summary>
        [DataMember(Name="color", EmitDefaultValue=false)]
        public string Color { get; set; }

        /// <summary>
        /// Gets or Sets Coordinates
        /// </summary>
        [DataMember(Name="coordinates", EmitDefaultValue=false)]
        public Coordinate Coordinates { get; set; }

        /// <summary>
        /// Gets or Sets Width
        /// </summary>
        [DataMember(Name="width", EmitDefaultValue=false)]
        public double? Width { get; set; }

        /// <summary>
        /// Gets or Sets Height
        /// </summary>
        [DataMember(Name="height", EmitDefaultValue=false)]
        public double? Height { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class PostIt {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  Contents: ").Append(Contents).Append("\n");
            sb.Append("  Color: ").Append(Color).Append("\n");
            sb.Append("  Coordinates: ").Append(Coordinates).Append("\n");
            sb.Append("  Width: ").Append(Width).Append("\n");
            sb.Append("  Height: ").Append(Height).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as PostIt);
        }

        /// <summary>
        /// Returns true if PostIt instances are equal
        /// </summary>
        /// <param name="input">Instance of PostIt to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(PostIt input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.Contents == input.Contents ||
                    (this.Contents != null &&
                    this.Contents.Equals(input.Contents))
                ) && 
                (
                    this.Color == input.Color ||
                    (this.Color != null &&
                    this.Color.Equals(input.Color))
                ) && 
                (
                    this.Coordinates == input.Coordinates ||
                    (this.Coordinates != null &&
                    this.Coordinates.Equals(input.Coordinates))
                ) && 
                (
                    this.Width == input.Width ||
                    (this.Width != null &&
                    this.Width.Equals(input.Width))
                ) && 
                (
                    this.Height == input.Height ||
                    (this.Height != null &&
                    this.Height.Equals(input.Height))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.Contents != null)
                    hashCode = hashCode * 59 + this.Contents.GetHashCode();
                if (this.Color != null)
                    hashCode = hashCode * 59 + this.Color.GetHashCode();
                if (this.Coordinates != null)
                    hashCode = hashCode * 59 + this.Coordinates.GetHashCode();
                if (this.Width != null)
                    hashCode = hashCode * 59 + this.Width.GetHashCode();
                if (this.Height != null)
                    hashCode = hashCode * 59 + this.Height.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
