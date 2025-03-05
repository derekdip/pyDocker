
type CardProps = {
    title: string;
    description: string;
    image: string;
};
export function Card(cardProps: CardProps) {
    const cardStyle = {
        border: '1px solid #ddd',
        borderRadius: '8px',
        overflow: 'hidden',
        width: '200px',
        boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
        transition: 'transform 0.3s ease',
    };
    const cardImageStyle = {
        width: '100%',
        height: 'auto',
    };
    
    const cardContentStyle = {
        padding: '16px',
    };
    
    const cardTitleStyle = {
        margin: '0',
        fontSize: '18px',
        fontWeight: 'bold',
    };
    
    const cardDescriptionStyle = {
        fontSize: '14px',
        color: '#555',
        marginTop: '8px',
    };
    
      return (
        <div style={cardStyle} className="card">
          <img src={cardProps.image} alt={cardProps.title} style={cardImageStyle} />
          <div style={cardContentStyle}>
            <h3 style={cardTitleStyle}>{cardProps.title}</h3>
            <p style={cardDescriptionStyle}>{cardProps.description}</p>
          </div>
        </div>
      );
  };