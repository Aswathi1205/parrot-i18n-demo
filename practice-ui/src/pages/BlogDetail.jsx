import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useTranslation } from "react-i18next";

function BlogDetail() {
  const { id } = useParams();
  const { t, i18n } = useTranslation();
  const [post, setPost] = useState(null);

  useEffect(() => {
    fetch(`/api/posts/${id}/?lang=${i18n.language}`)
      .then((response) => response.json())
      .then((data) => {
        setPost(data);
      });
  }, [id, i18n.language]);

  if (!post) {
    return <p>{t("loading")}</p>;
  }

  return (
    <div>
        
      <h1>{post.title}</h1>

      <p>{post.body}</p>

      <p>
        {t("published")}: {post.publish_date}
      </p>
    </div>
  );
}

export default BlogDetail;